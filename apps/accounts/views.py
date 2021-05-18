from django.contrib import messages, auth
from django.http.response import HttpResponse
from .forms import RegistrationForm
from django.shortcuts import redirect, render
from .models import Account
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = ''.join(email.split('@'))
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()

            # Correo activacion de usuario

            current_site = get_current_site(request)
            mail_subject = 'Porfavor activa tu cuenta - MusicPro.cl'
            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                # Encriptar PK del usuario
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # Crea un token para el usuario
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            # messages.success(
            #     request, 'Registro exitoso porfavor revise su correo electrónico')
            return redirect('/accounts/login/?command=verification&email='+email)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Has iniciado sesión exitosamente.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Datos incorrectos. Intente nuevamente')
            return redirect('login')
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Has cerrado sesión correctamente')
    return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()  # pk usuario
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Has confirmado tu cuenta correctamente')
        return redirect('login')
    else:
        messages.error(request, 'Link de activación inválido')
        return redirect('register')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Correo Restaurar contraseña
            current_site = get_current_site(request)
            mail_subject = 'Recuperar contraseña - MusicPro.cl'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                # Encriptar PK del usuario
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # Crea un token para el usuario
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(
                request, 'Se ha enviado un correo con indicaciones para que puedas recuperar tu contraseña')
            return redirect('login')
        else:
            messages.error(request, 'La cuenta no existe')
            return redirect('forgotPassword')
    return render(request, 'accounts/forgotPassword.html')


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()  # pk usuario
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Porfavor reestablece tu contraseña.')
        return redirect('resetPassword')
    else:
        messages.error(
            request, 'El link para reestablecer tu cuenta ha expirado.')
        return redirect('login')


def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(
                request, 'La contraseña se ha reestablecido exitosamente')
            return redirect('login')

        else:
            messages.error(request, 'La contraseña no coincide')
            return redirect('resetPassword')
    else:
        return render(request, 'accounts/resetPassword.html')

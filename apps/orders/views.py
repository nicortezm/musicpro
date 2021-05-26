from django.db.models.enums import Choices
from orders.models import Payment
from django.http.response import HttpResponseRedirect
from orders.models import Order
from orders.forms import OrderForm
from django.shortcuts import redirect, render
from carts.models import CartItem
from django.conf import settings
import datetime
import random
from transbank.common.options import WebpayOptions
from transbank.common.integration_type import IntegrationType
from transbank.webpay.webpay_plus.transaction import Transaction
from carts.views import _cart_id
from carts.models import Cart
from accounts.models import Account
from datetime import date
from django.views.decorators.csrf import csrf_exempt


urlSite = 'http://127.0.0.1:8000/'

# Create your views here.
Desc = settings.DESCUENTO

@csrf_exempt
def place_order(request, total=0, quantity=0):
    current_user = request.user

    # si el contador de carrito es igual a 0, redirigir a la tienda


    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')


    grand_total = 0
    descuento = 0

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

        if (quantity >= 4):
            descuento = int((Desc * total)/100)
        grand_total = total - descuento
        


    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # guardar la información dentro del modelo orden
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.email = form.cleaned_data['email']
            data.region = form.cleaned_data['region']
            data.comuna = form.cleaned_data['comuna']
            data.calle = form.cleaned_data['calle']
            data.num_calle = form.cleaned_data['num_calle']
            data.block = form.cleaned_data['block']
            data.num_dpto = form.cleaned_data['num_dpto']
            data.comentarios = form.cleaned_data['comentarios']
            data.order_total = grand_total
            data.descuento = descuento
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            # Generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d") #20210505
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user,is_ordered=False,order_number=order_number)
            buy_order = order.order_number
            session_id = 123123
            amount = order.order_total
            return_url = urlSite + 'pedidos/confirm/'
            response = Transaction.create(buy_order, session_id, amount, return_url)
            context = {
                'response':response,
                'order':order,
                'cart_items': cart_items,
                'total': total,
                'descuento': descuento,
                'grand_total': grand_total,
            }


            return render(request,'orders/payments.html',context)
    else:
        return redirect('checkout')
@csrf_exempt
def WebpayConfirm(request):
    quantity = 0
    total = 0
    descuento = 0
    grand_total = 0
    today = date.today()
    fecha = today.strftime("%d/%m/%Y")
    if request.POST['token_ws']:
        token = request.POST['token_ws']
        response = Transaction.commit(token)
        user = Account.objects.get(email="nicoigcor@gmail.com")
        order = Order.objects.get(user=user,is_ordered=False)
        print(user)
        # if request.user.is_authenticated:
        pago = Payment.objects.create(user=user,payment_id=order.order_number,payment_method="WebPay",amount_paid=response.amount,status=response.status)
        
        if response.response_code == 0 and response.status == 'AUTHORIZED':
            order.payment = pago
            order.is_ordered = True
            order.status = "Aceptada"
            order.save()
            cart_items = CartItem.objects.filter(user=user)
            for cart_item in cart_items:
                total += (cart_item.product.price * cart_item.quantity)
                quantity += cart_item.quantity
            if (quantity >= 4):
                descuento = int((Desc * total)/100)
            grand_total = total - descuento
        context = {
            'token': token,
            'response': response,
            'fecha': fecha,
            'cart': cart_items,
            'total': total,
            'descuento': descuento,
            'grand_total': grand_total
            }

            
        # TODO: 
        # Mover los items comprados a la Tabla productos pedidos
        # Disminuir la cantidad de productos vendidos
        # Limpiar el carrito
        # Enviar email al comprador
        # Fixear el CSRF token en las cookies para evitar el logout



    elif request.POST['TBK_TOKEN']:
        tbk_token = request.POST['TBK_TOKEN']
        tbk_orden_compra = request.POST['TBK_ORDEN_COMPRA']
        tbk_id_sesion = request.POST['TBK_ID_SESION']
        context = {
            'tbk_token': tbk_token,
            'tbk_orden_compra': tbk_orden_compra,
            'tbk_id_sesion': tbk_id_sesion
        }
    else:
        context = {'error':'Malito'}
    return render(request, 'orders/confirm.html',context)


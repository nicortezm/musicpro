from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'password',
    }))

    first_name = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'text',
    }))
    last_name = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'text',
    }))
    email = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'email',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleanned_data = super(RegistrationForm, self).clean()
        password = cleanned_data.get('password')
        confirm_password = cleanned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Las contraseñas deben ser iguales!'
            )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

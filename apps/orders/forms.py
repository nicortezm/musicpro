from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','email','region','comuna','calle','num_calle','block','num_dpto','comentarios',]
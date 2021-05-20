from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import Guest
# Create your views here.

def _guest_id(request):
    guest = request.session.session_key
    if not guest:
        guest = request.session.create()
    return guest

def guest(request, cart):
    try:
        guest = Guest.objects.get(guest_id=_guest_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        if request.user.is_authenticated:
            descuento = int((4 * total)/100)
        grand_total = total - descuento
    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'descuento': descuento,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)

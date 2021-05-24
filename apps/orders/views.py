from orders.models import Order
from orders.forms import OrderForm
from django.shortcuts import redirect, render
from carts.models import CartItem
from django.conf import settings
import datetime
# Create your views here.
Desc = settings.DESCUENTO


def payments(request):
    return render(request,'orders/payments.html')


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
            context = {
                'order':order,
                'cart_items': cart_items,
                'total': total,
                'descuento': descuento,
                'grand_total': grand_total,
            }


            return render(request,'orders/payments.html',context)
    else:
        return redirect('checkout')
from django.shortcuts import render
from apps.tienda.models import Product
# Create your views here.


def home(request):
    products = Product.objects.all().filter(
        is_available=True).order_by('-id')[:12]
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)

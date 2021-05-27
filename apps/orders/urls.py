from django.urls import path
from . import views

urlpatterns = [
    path('realizar_pedido/',views.place_order, name='place_order'),
    path('confirm/', views.WebpayConfirm, name='confirm'),

]


from apps.tienda.models import Variation,Product
from django.db import models
from apps.accounts.models import Account
# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250,blank = True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'

    
class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE,null=True,verbose_name="usuario")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="producto")
    variations = models.ManyToManyField(Variation,blank=True,verbose_name="Variaciones")
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True,verbose_name="carrito")
    quantity = models.IntegerField("Cantidad")
    is_active = models.BooleanField(default=True,verbose_name="¿Está activo?")

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product
    class Meta:
        verbose_name = 'ItemCarrito'
        verbose_name_plural = 'ItemCarritos'
    
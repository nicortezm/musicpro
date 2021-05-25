from tienda.models import Product, Variation
from accounts.models import Account
from django.db import models

# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE,verbose_name="usuario",blank=True)
    payment_id = models.CharField("id pago",max_length=100)
    payment_method = models.CharField("metodo de pago",max_length=100) # Por ahora solo webpay
    amount_paid = models.IntegerField("monto pagado") # Monto total pagado
    status = models.CharField("estado",max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'pago'
        verbose_name_plural = 'pagos'

    def __str__(self):
        return self.payment_id

class Order(models.Model):
    STATUS = (
        ('Nueva', 'Nueva'),
        ('Aceptada', 'Aceptada'),
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada'),
    )

    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True,verbose_name="usuario")
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True,verbose_name="id pago")
    order_number = models.CharField("numero de orden",max_length=20)
    first_name = models.CharField("nombre",max_length=50)
    last_name = models.CharField("apellido",max_length=50)
    email = models.EmailField(max_length=50)
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    num_calle = models.CharField(max_length=50)
    block = models.CharField(max_length=10, blank=True)
    num_dpto = models.CharField(max_length=10, blank=True)
    comentarios = models.CharField(max_length=100, blank=True)
    order_total = models.IntegerField("total orden")
    descuento = models.IntegerField()
    status = models.CharField("estado",max_length=10, choices=STATUS, default='Nueva')
    ip = models.CharField(blank=True, max_length=20)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    def full_name(self):

        return f'{self.first_name} {self.last_name}'

    def full_address(self):
        
        if len(self.block) > 0:
            return f'{self.calle} #{self.num_calle} BLOCK:{self.block} DPTO:{self.num_dpto}'
        else:
            return f'{self.calle} #{self.num_calle} {self.num_dpto}'

    def __str__(self):
        return self.first_name

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name="orden")
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True,verbose_name="id pago") # Solo webpay
    user = models.ForeignKey(Account, on_delete=models.CASCADE,verbose_name="usuario")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="producto")
    variations = models.ManyToManyField(Variation, blank=True,verbose_name="variaciones")
    quantity = models.IntegerField("cantidad")
    product_price = models.FloatField("precio producto")
    ordered = models.BooleanField("¿Completado?",default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Producto pedido'
        verbose_name_plural = 'Productos pedidos'

    def __str__(self):
        return self.product.product_name

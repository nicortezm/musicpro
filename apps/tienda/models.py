from typing import DefaultDict
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    category_name = models.CharField("Nombre categoria",max_length=50,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField("Descripcion",max_length=255,blank=True)
    cat_image = models.ImageField("Imagen categoria",upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField("nombre producto",max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField("descripcion",max_length=500,blank=True)
    price = models.IntegerField("precio")
    images = models.ImageField("imagenes",upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField("disponible",default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name = 'Categoria')

    # Agregar Foreingkey marca.
    # Agregar serial.
    created_date = models.DateField("Fecha creación",auto_now_add=True)
    modified_date = models.DateField("Fecha modificación",auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.product_name


variation_category_choice = (
    ('color','Color'),
    ('size','Tamaño')
)
class Variation(models.Model):
    product = models.ForeignKey(Product,verbose_name="Producto",on_delete=models.CASCADE)
    variation_category = models.CharField("Categoría variación",max_length=100,choices=variation_category_choice)
    variation_value = models.CharField("Valor variación",max_length=100)
    is_active = models.BooleanField("¿Está activa?",default=True)
    created_date = models.DateTimeField("Fecha de creación",auto_now_add=True)

    def __unicode__(self):
        return self.product
    
    class Meta:
        verbose_name = 'Variación'
        verbose_name_plural = 'Variaciones'
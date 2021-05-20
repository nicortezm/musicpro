from django.db import models

# Create your models here.

class Guest(models.Model):
    guest_id = models.CharField(max_length=250,blank = True)
    first_name = models.CharField("nombre", max_length=50)  
    last_name = models.CharField("apellido", max_length=50)
    email = models.EmailField("correo", max_length=100, unique=True)
    region = models.CharField("region", max_length=50)
    comuna = models.CharField("comuna", max_length=50)
    calle = models.CharField("calle", max_length=100)
    num_calle = models.CharField("Num. Calle", max_length=10)
    block = models.CharField("block", max_length=20)
    num_dpto = models.CharField("Num. Dpto", max_length=10)
    comentarios = models.CharField("comentarios", max_length=100)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.guest_id
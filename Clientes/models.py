from django.db import models
from Productos.models import Producto


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    idd = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    carrito = models.ManyToManyField(Producto)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)
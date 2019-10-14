from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.FloatField(null=True, blank=True, default=None)
    talla = models.FloatField(null=True, blank=True, default=None)
    cantidad = models.FloatField(null=True, blank=True, default=None)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)
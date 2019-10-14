from rest_framework import serializers
from . import models


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'nombre','marca', 'precio','talla','cantidad','descripcion',)
        model = models.Producto


from rest_framework import serializers
from . import models


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ( 'nombre' ,'idd' ,'direccion' , 'correo',  'carrito' ,)
        model = models. Cliente


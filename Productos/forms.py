from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'marca',
            'precio',
            'talla',
            'cantidad',
            'descripcion',
        ]

        labels = {
            'nombre' : 'Nombre',
            'marca' : 'Marca',
            'precio' : 'Precio',
            'talla' : 'Talla',
            'cantidad' :'Cantidad',
            'descripcion' : 'Descripcion',
        }


from django import forms
from .models import Inventario

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = [
            'referencia',
            'cantidad',
        ]

        labels = {
            'referencia' : 'Referencia',
            'cantidad' : 'Cantidad',

        }


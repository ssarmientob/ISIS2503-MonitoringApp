from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre' ,
            'idd' ,
            'direccion' ,
            'correo',

        ]

        labels = {
            'nombre' : 'Nombre',
            'idd'  :'Documento',
            'direccion' : 'Direccion' ,
            'correo' : 'Correo',

        }


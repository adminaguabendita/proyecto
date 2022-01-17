from re import A
from tkinter import Widget
from django import forms
#Libreria para validar formularios
from django.core import validators

#Clase que Hereda de forms.Form
class FormTiendas(forms.Form):
    co = forms.CharField(
        label = "Centro Operacion",
        required = True,
        max_length = 3,
        min_length = 3,
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Ingresa el CO'
            }
        )
    )
    descripcion = forms.CharField(
        label = "Descripción",        
    )
   
    
    
    
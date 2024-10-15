from django import forms 
from .forms import*
from .models import Producto

class agregar_producto_form(forms.ModelForm):
    class Meta: 
        model = Producto 
        fields = '__all__'


    
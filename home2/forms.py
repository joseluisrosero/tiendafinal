from django import forms 
from .forms import*
from .models import*


class contacto_form(forms.Form):
    correo = forms.EmailField(widget= forms.TextInput())
    titulo = forms.CharField(widget= forms.TextInput())
    texto = forms.CharField(widget= forms.Textarea())
    
class agregar_producto_form(forms.ModelForm):
    class Meta: 
        model = Producto 
        fields = '__all__'


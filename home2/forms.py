from django import forms

class contacto_form(forms.Form):

    correo =forms.EmailField(widget=forms.TextInput)
    Titulo =forms.CharField(widget=forms.TextInput)
    texto =forms.EmailField(widget=forms.Textarea)
    
from django import forms

class LoginFormulario(forms.Form):
    usuario =  forms.CharField(max_length=50)
    contrasenia = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    
    
class BusquedaFormulario(forms.Form):
    usuario =  forms.CharField(max_length=50, required=False)
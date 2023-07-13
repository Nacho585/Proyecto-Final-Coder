from django import forms

class EstacionFormulario(forms.Form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()

class SensorFormulario(forms.Form):
    nombre = forms.CharField()
    nivel = forms.IntegerField()

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

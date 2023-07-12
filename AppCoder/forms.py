from django import forms

class EstacionFormulario(forms.Form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()


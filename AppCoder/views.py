from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estacion,  sensorShampoo, Usuario

# Create your views here.

"""def estacion(self):

    estacion = Estacion(nombre="Santa ana", codigo="2")
    estacion.save()
    documentoDeTexto = f"--->Estacion = {estacion.nombre} Codigo = {estacion.codigo}" 

    return HttpResponse(documentoDeTexto)"""

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def estacion(request): 
    return render(request, 'AppCoder/estacion.html')

def sensorshampoo(request):
    return render(request, 'AppCoder/sensorshampoo.html')

def usuario(request):
    return render(request, 'AppCoder/usuario.html')
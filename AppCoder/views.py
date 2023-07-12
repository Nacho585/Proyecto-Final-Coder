from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estacion,  sensorShampoo, Usuario

# Create your views here.

def estacion(self):

    estacion = Estacion(nombre="Santa ana", codigo="2")
    estacion.save()
    documentoDeTexto = f"--->Estacion = {estacion.nombre} Codigo = {estacion.codigo}" 

    return HttpResponse(documentoDeTexto)
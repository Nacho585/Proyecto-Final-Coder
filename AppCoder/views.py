from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estacion,  sensorShampoo, Usuario
from AppCoder.forms import EstacionFormulario

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

def estacionFormulario(request):
    if request.method == 'POST':
        miFormulario = EstacionFormulario(request.POST) # aca llega la info del HTML
        print(miFormulario) #Para q servia esto

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            estacion = Estacion(nombre=informacion['nombre'], codigo=informacion['codigo'])
            estacion.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = EstacionFormulario()

    return render(request, "AppCoder/estacionFormulario.html", {"miFormulario": miFormulario})


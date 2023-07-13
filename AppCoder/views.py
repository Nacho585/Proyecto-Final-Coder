from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estacion,  sensorShampoo, Usuario
from AppCoder.forms import EstacionFormulario , UsuarioFormulario , SensorFormulario

# Create your views here.

"""def estacion(self):

    estacion = Estacion(nombre="Santa ana", codigo="2")
    estacion.save()
    documentoDeTexto = f"--->Estacion = {estacion.nombre} Codigo = {estacion.codigo}" 

    return HttpResponse(documentoDeTexto)"""

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def estacion(request): 
    estaciones = Estacion.objects.all()
    return render(request, 'AppCoder/estacion.html', {'estaciones': estaciones})

def sensorshampoo(request):
    sensores = sensorShampoo.objects.all()
    return render(request, 'AppCoder/sensorshampoo.html', {'sensores' : sensores})

def usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'AppCoder/usuario.html' , {'usuarios' : usuarios})

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

def sensorFormulario(request):
    if request.method == 'POST':
        miFormulario = SensorFormulario(request.POST) # aca llega la info del HTML
        print(miFormulario) #Para q servia esto

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            sensor = sensorShampoo(nombre=informacion['nombre'], nivel=informacion['nivel'])
            sensor.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = SensorFormulario()

    return render(request, "AppCoder/sensorFormulario.html", {"miFormulario": miFormulario})

def usuarioFormulario(request):
    if request.method == 'POST':
        miFormulario = UsuarioFormulario(request.POST) # aca llega la info del HTML
        print(miFormulario) #Para q servia esto

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            usuario = Usuario(nombre=informacion['nombre'], apellido=informacion['apellido'] , email=informacion['email'])
            usuario.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = UsuarioFormulario()

    return render(request, "AppCoder/usuarioFormulario.html", {"miFormulario": miFormulario})




from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estacion,  sensorShampoo, Usuario
from AppCoder.forms import EstacionFormulario , UsuarioFormulario , SensorFormulario
from django.contrib.auth.decorators import login_required
from Login.models import Avatar
from Login.forms import *


# Create your views here.

"""def estacion(self):

    estacion = Estacion(nombre="Santa ana", codigo="2")
    estacion.save()
    documentoDeTexto = f"--->Estacion = {estacion.nombre} Codigo = {estacion.codigo}" 

    return HttpResponse(documentoDeTexto)"""


def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'AppCoder/inicio.html')

def about(request):
    return render(request, 'AppCoder/about.html')

@login_required
def estacion(request): 
    estaciones = Estacion.objects.all()
    return render(request, 'AppCoder/estacion.html', {'estaciones': estaciones})

@login_required
def sensorshampoo(request):
    sensores = sensorShampoo.objects.all()
    return render(request, 'AppCoder/sensorshampoo.html', {'sensores' : sensores})

@login_required
def usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'AppCoder/usuario.html' , {'usuarios' : usuarios})

@login_required
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

@login_required
def eliminarEstacion(request, estacion_nombre):

    estacion = Estacion.objects.filter(nombre=estacion_nombre).first()
    estacion.delete()

    estaciones = Estacion.objects.all()

    return render (request, "AppCoder/estacion.html", {"estaciones":estaciones})

@login_required
def editarEstacion(request, estacion_nombre):
    estacion = Estacion.objects.filter(nombre=estacion_nombre).first()

    if request.method == "POST":
        miFormulario = EstacionFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            estacion.nombre = informacion['nombre']
            estacion.codigo = informacion['codigo']

            estacion.save()
            return render (request, "AppCoder/inicio.html")
    
    else:
        miFormulario = EstacionFormulario(initial={'nombre': estacion.nombre, 'codigo': estacion.codigo})

    return render (request, "AppCoder/editarEstacion.html", {"miFormulario":miFormulario,"estacion_nombre":estacion_nombre})

@login_required
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

@login_required
def eliminarSensor(request, sensor_nombre):

    sensor = sensorShampoo.objects.filter(nombre=sensor_nombre).first()
    sensor.delete()

    sensores = sensorShampoo.objects.all()

    return render (request, "AppCoder/sensorshampoo.html", {"sensores":sensores})

@login_required
def editarSensor(request, sensor_nombre):
    sensor = sensorShampoo.objects.filter(nombre=sensor_nombre).first()

    if request.method == "POST":
        miFormulario = SensorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            sensor.nombre = informacion['nombre']
            sensor.nivel = informacion['nivel']

            sensor.save()
            return render (request, "AppCoder/inicio.html")
    
    else:
        miFormulario = SensorFormulario(initial={'nombre': sensor.nombre, 'nivel': sensor.nivel})

    return render (request, "AppCoder/editarSensor.html", {"miFormulario":miFormulario,"sensor_nombre":sensor_nombre})

@login_required
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

@login_required
def eliminarUsuario(request, usuario_nombre):

    usuario = Usuario.objects.filter(nombre=usuario_nombre).first()
    usuario.delete()

    usuarios = Usuario.objects.all()

    return render (request, "AppCoder/usuario.html", {"usuarios":usuarios})

@login_required
def editarUsuario(request, usuario_nombre):
    usuario = Usuario.objects.filter(nombre=usuario_nombre).first()

    if request.method == "POST":
        miFormulario = UsuarioFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            usuario.nombre = informacion['nombre']
            usuario.apellido = informacion['apellido']
            usuario.email = informacion['email']

            usuario.save()
            return render (request, "AppCoder/inicio.html")
    
    else:
        miFormulario = UsuarioFormulario(initial={'nombre': usuario.nombre, 'apellido': usuario.apellido , 'email': usuario.email})

    return render (request, "AppCoder/editarUsuario.html", {"miFormulario":miFormulario,"usuario_nombre":usuario_nombre})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario=AvatarFormulario()
        
    return render(request, "AppCoder/agregarAvatar.html", {'miFormulario': miFormulario})
    

# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm 
from django.contrib.auth import login, logout, authenticate
from Login.forms import UserRegisterForm , UserEditForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "Login/login.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "Login/login.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Login/login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:   
            form = UserRegisterForm()     

      return render(request,"AppCoder/inicio.html" ,  {"form":form})

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

    return render(request, "Login/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

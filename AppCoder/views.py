from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpRequest
from AppCoder.forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.


def inicio(request):
    return render (request, "AppCoder/inicio.html")

def sobrenosotros(request):
    return render (request, "AppCoder/img/sobrenosotros.html")

def usuarios(request):
    return render(request, "AppCoder/usuarios.html")

def blog(request):
    return render(request, "AppCoder/blog.html")

def staff(request):
    return render(request, "AppCoder/staff.html")

def form_usuarios(request):
    if request.method=="POST":
        form=UsuariosForm(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            nickname=informacion["nickname"]
            email=informacion["email"]
            usuario = Usuarios(nombre=nombre, apellido=apellido,nickname=nickname, email=email)
            usuario.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        formulario=UsuariosForm()
        return render (request, "AppCoder/form_usuarios.html", {"formulario":formulario})

def form_staff(request):
    if request.method=="POST":
        form=StaffForm(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            nickname=informacion["nickname"]
            email=informacion["email"]
            area_control = informacion ['area_control']
            profesion = informacion ['profesion']
            staff = Staff(nombre=nombre, apellido=apellido,nickname=nickname, email=email, area_control=area_control, profesion=profesion)
            staff.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        formulario=StaffForm()
        return render (request, "AppCoder/form_staff.html", {"formulario":formulario})

def form_blog(request):
    if request.method=="POST":
        form=blogForm(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data
            titulo=informacion["titulo"]
            cuerpo=informacion["cuerpo"]
            foto=informacion["foto"]
            temas = blog(titulo=titulo, cuerpo=cuerpo , foto=foto)
            temas.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        formulario=blogForm()
        return render (request, "AppCoder/form_blog.html", {"formulario":formulario})

def busco_usuarios(request):
    return render(request, 'AppCoder/busco_usuarios.html')

def buscando_usuarios(request):
    if request.GET['nickname']:
        nickname = request.GET['nickname']
        usuarios=Usuarios.objects.filter(nickname=nickname)
        return render(request, 'AppCoder/res_b_usuarios.html', {'usuarios': usuarios})
    else:
        return render(request, 'AppCoder/busco_usuarios.html', {'mensaje': 'Ingrese un usuario'})


def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'AppCoder/inicio.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppCoder/login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})

                
    else:
        form=AuthenticationForm()
        return render(request, "AppCoder/login.html", {"formulario":form})

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppCoder/register.html", {"formulario":form, "mensaje":"FORMULARIO INVALIDO"})

    else:
        form=UserRegisterForm()
        return render(request, "AppCoder/register.html", {"formulario":form})

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppCoder/register.html", {"formulario":form, "mensaje":"FORMULARIO INVALIDO"})

    else:
        form=UserRegisterForm()
        return render(request, "AppCoder/register.html", {"formulario":form})

@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":"Perfil editado correctamente"})
        else:
            return render(request, "AppCoder/editarPerfil.html", {"formulario":form, "usuario":usuario, "mensaje":"FORMULARIO INVALIDO"})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, "AppCoder/editarPerfil.html", {"formulario":form, "usuario":usuario (request)})



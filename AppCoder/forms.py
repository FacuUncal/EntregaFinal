from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class UsuariosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    nickname = forms.CharField(max_length=50)
    email = forms.EmailField()

class blogForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    cuerpo = forms.CharField(max_length=5000)
    foto = forms.ImageField ()

class StaffForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    nickname = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)
    area_control = forms.CharField(max_length=50)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

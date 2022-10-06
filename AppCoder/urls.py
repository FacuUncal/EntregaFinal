
from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("usuarios/", usuarios, name="usuarios"),
    path("blog/", blog, name="blog"),
    path("sn/", sobrenosotros, name="sobrenosotros"),
    path("staff/", staff, name="staff"),
    path("", inicio, name="inicio"),
    path('form_usuarios/', form_usuarios, name='form_usuarios'),
    path('form_staff/', form_staff, name= 'form_staff'),
    path('form_blog/', form_blog, name= 'form_blog'),
    path('busco_usuarios/', busco_usuarios, name= 'busco_usuarios'),
    path('buscando_usuarios/', buscando_usuarios, name ='buscando_usuarios'),

  #login register logout
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil')
]
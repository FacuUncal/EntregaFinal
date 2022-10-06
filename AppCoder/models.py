from django.db import models

# Create your models here.

#El modelo 'Usuarios' es para almacenar los datos de los que se logean
class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre+' '+self.apellido+' nickname: '+self.nickname 

#El modelo 'Temas' almacena los gustos de los usuarios. Se pueden editar a gusto
class blog(models.Model):
    titulo = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=5000)
    foto = models.ImageField ()


    
#El modelo 'Staff' mostrara informacion de los admins de cada area
class Staff(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    area_control = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50,default='DEFAULT VALUE')
    email = models.EmailField(default='DEFAULT VALUE')

    def __str__(self):
        return self.nombre+' '+self.apellido+' '+self.nickname+' '+self.profesion



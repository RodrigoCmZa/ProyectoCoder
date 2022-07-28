import email
from tabnanny import verbose
from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre} - {self.camada}'

    class Meta():
        verbose_name = 'Course' # cambiar nombre en base de datos
        verbose_name_plural = 'My Courses'
        ordering = ('nombre', '-camada') # ordenar lista en base de datos
        unique_together = ('nombre', 'camada') # sirve para no repetir lo que ya existe


class Estudiante(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.nombre} - {self.apellido}'


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default =1) #si se elimina un registro de la tabla primaria, se elimina de la secundaria


from django.db import models

# Create your models here.

class Estacion(models.Model):

    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()

    def __str__(self):
        return f"Nombre estacion: {self.nombre} - Codigo: {self.camada}"

class sensorShampoo(models.Model):
    nombre = models.CharField(max_length=20)
    nivel = models.IntegerField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()


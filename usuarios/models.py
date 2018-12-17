from django.db import models

# Create your models here.
from departamentos.models import Departamento
from municipios.models import Municipio


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    foto = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    genero = models.CharField(max_length=15)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

from django.db import models

# Create your models here.
from lugares.models import Lugar


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    foto = models.CharField(max_length=100)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
from usuarios.models import Usuario


class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombre_lugar=models.CharField(max_length=100)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=15)
    email = ArrayField(ArrayField(models.CharField(max_length=50, blank=True)))
    informacion = models.CharField(max_length=200)
    nit = models.IntegerField()
    aceptado = models.BooleanField(default=False)

    def __unicode__(self):
        return self.informacion

    def __str__(self):
        return self.informacion


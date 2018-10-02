from django.db import models

# Create your models here.
from lugares.models import Lugar
from usuarios.models import Usuario


class Visita(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ManyToManyField(Usuario)
    lugar = models.ManyToManyField(Lugar)

    def __unicode__(self):
        return self.lugar.nombre

    def __str__(self):
        return self.lugar.nombre

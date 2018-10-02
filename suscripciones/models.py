from django.db import models

# Create your models here.
from lugares.models import Lugar
from usuarios.models import Usuario


class Suscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ManyToManyField(Usuario)
    lugar = models.ManyToManyField(Lugar)
    fecha_suscripcion = models.DateTimeField()
    notificaciones = models.BooleanField(default=True)

    def __unicode__(self):
        return self.lugar.nombre

    def __str__(self):
        return self.lugar.nombre
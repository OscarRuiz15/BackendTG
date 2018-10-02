from django.db import models

# Create your models here.
from lugares.models import Lugar
from usuarios.models import Usuario


class Suscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    fecha_suscripcion = models.DateField()
    hora_suscripcion = models.TimeField()
    notificaciones = models.BooleanField(default=True)

    def __unicode__(self):
        return self.lugar.nombre

    def __str__(self):
        return self.lugar.nombre
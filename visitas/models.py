from django.db import models
from rest_framework.reverse import reverse as api_reverse

# Create your models here.
from lugares.models import Lugar
from usuarios.models import Usuario


class Visita(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    fecha_visita = models.DateField()
    hora_visita = models.TimeField()

    def get_api_url(self, request=None):
        return api_reverse("api-visitas:visitas-rud", kwargs={'id': self.id}, request=request)

    def __unicode__(self):
        return self.lugar.nombre

    def __str__(self):
        return self.lugar.nombre

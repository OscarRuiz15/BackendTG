from django.db import models
from rest_framework.reverse import reverse as api_reverse

# Create your models here.
from comentarios.models import Comentario
from lugares.models import Lugar


class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    lugar=models.ForeignKey(Lugar, on_delete=models.CASCADE)
    comentario=models.ManyToManyField(Comentario, blank=True)
    direccion=models.CharField(max_length=100)
    foto=models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=2, decimal_places=1)
    tipo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    finalizado = models.BooleanField(default=False)

    def get_api_url(self, request=None):
        return api_reverse("api-eventos:evento-rud", kwargs={'id': self.id}, request=request)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre
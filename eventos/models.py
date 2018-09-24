from django.db import models

# Create your models here.
from comentarios.models import Comentario
from lugares.models import Lugar


class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    lugar=models.OneToOneField(Lugar, on_delete=models.CASCADE)
    comentario=models.ManyToManyField(Comentario)
    direccion=models.CharField(max_length=100)
    foto=models.CharField(max_length=100)#models.ManyToManyField()
    calificacion = models.DecimalField(max_digits=2, decimal_places=1)
    tipo = models.CharField(max_length=100)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    dia_inicio = models.CharField(max_length=15)
    mes_inicio = models.CharField(max_length=15)
    finalizado = models.BooleanField(default=False)
    dia_semana=models.CharField(max_length=10)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre
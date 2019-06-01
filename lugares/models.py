from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
from categorias.models import Categoria
from comentarios.models import Comentario
from tags.models import Tag
from usuarios.models import Usuario

from rest_framework.reverse import reverse as api_reverse


class Lugar(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    foto = ArrayField(models.CharField(max_length=150, blank=True))
    calificacion = models.DecimalField(max_digits=30, decimal_places=25)
    tag = models.ManyToManyField(Tag)
    email = ArrayField(models.CharField(max_length=100, blank=True))
    sitio_web = ArrayField(models.CharField(max_length=50, blank=True))
    telefono = ArrayField(models.CharField(max_length=15, blank=True))
    redes = ArrayField(models.CharField(max_length=50, blank=True))
    comentario = models.ManyToManyField(Comentario, blank=True)
    direccion = models.CharField(max_length=100)
    hora_abierto = ArrayField(models.CharField(max_length=100, default='{06:00:00, 06:00:00, 06:00:00, 06:00:00, 06:00:00, 06:00:00, 06:00:00}'))
    hora_cerrado = ArrayField(models.CharField(max_length=100, default='{22:00:00, 22:00:00, 22:00:00, 22:00:00, 22:00:00, 22:00:00, 22:00:00}'))
    dias_servicio = ArrayField(models.CharField(max_length=100, default='{Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo}'))
    latitud=models.DecimalField(max_digits=40, decimal_places=20)
    longitud=models.DecimalField(max_digits=40, decimal_places=20)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    propietario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateField()
    municipio = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)

    def get_api_url(self, request=None):
        return api_reverse("api-lugar:lugar-rud", kwargs={'id': self.id}, request=request)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

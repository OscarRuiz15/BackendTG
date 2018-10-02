from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
from categorias.models import Categoria
from comentarios.models import Comentario
from productos.models import Producto
from tags.models import Tag
from usuarios.models import Usuario


class Lugar(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    foto = ArrayField(models.CharField(max_length=150, blank=True))
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=2, decimal_places=1)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    email = ArrayField(models.CharField(max_length=100, blank=True))
    sitio_web = ArrayField(models.CharField(max_length=50, blank=True))
    telefono = ArrayField(models.CharField(max_length=15, blank=True))
    redes = ArrayField(models.CharField(max_length=50, blank=True))
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    hora_abierto = models.TimeField()
    hora_cerrado = models.TimeField()
    dias_servicio=models.CharField(max_length=100)
    latitud=models.DecimalField(max_digits=20, decimal_places=10)
    longitud=models.DecimalField(max_digits=20, decimal_places=10)
    municipio=models.CharField(max_length=100)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    propietario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateField()

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

from django.db import models
from usuarios.models import Usuario
# Create your models here.

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=200)
    usuario = models.ManyToManyField(Usuario)
    fecha = models.DateTimeField()
    calificacion = models.DecimalField(max_digits=2, decimal_places=1)

    def __unicode__(self):
        return self.mensaje

    def __str__(self):
        return self.mensaje
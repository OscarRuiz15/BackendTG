from django.db import models
from usuarios.models import Usuario
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Preferencia(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=100, default='{}'))

    def __unicode__(self):
        return self.usuario.nombre

    def __str__(self):
        return self.usuario.nombre

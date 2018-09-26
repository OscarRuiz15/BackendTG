from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    uid= models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    email=models.EmailField()
    foto = models.CharField(max_length=100)
    fecha_nacimiento=models.DateField()
    telefono=models.CharField(max_length=15)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre
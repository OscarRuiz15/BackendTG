from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    #descripcion = models.CharField(max_length=200)
    foto = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre
from django.db import models


class Departamento(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre


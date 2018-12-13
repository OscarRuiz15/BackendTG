from django.db import models

from departamentos.models import Departamento


class Municipio(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

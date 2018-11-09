from django.db import models
from lugares.models import Lugar
from usuarios.models import Usuario

# Create your models here.
class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre
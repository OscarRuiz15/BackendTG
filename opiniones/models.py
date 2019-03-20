from django.db import models
from usuarios.models import Usuario
from lugares.models import Lugar

# Create your models here.
class Opinion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.id
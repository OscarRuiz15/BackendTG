from django.db import models
from usuarios.models import Usuario
from rest_framework.reverse import reverse as api_reverse
# Create your models here.

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    calificacion = models.DecimalField(max_digits=2, decimal_places=1)

    def get_api_url(self, request=None):
        return api_reverse("api-comments:comments-rud", kwargs={'id': self.id}, request=request)

    def __unicode__(self):
        return self.mensaje

    def __str__(self):
        return self.mensaje
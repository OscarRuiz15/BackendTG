from django.db import models
from rest_framework.reverse import reverse as api_reverse
# Create your models here.


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    foto = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    genero = models.CharField(max_length=15)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)

    def get_api_url(self, request=None):
        return api_reverse("api-users:users-rud", kwargs={'uid': self.uid}, request=request)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

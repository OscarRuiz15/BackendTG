from django.db import models
from rest_framework.reverse import reverse as api_reverse

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    foto = models.CharField(max_length=100)

    def get_api_url(self, request=None):
        return api_reverse("api-category:categories-rud", kwargs={'id': self.id}, request=request)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre
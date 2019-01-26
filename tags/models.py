from django.db import models
from rest_framework.reverse import reverse as api_reverse

# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def get_api_url(self, request=None):
        return api_reverse("api-tags:tags-rud", kwargs={'id': self.id}, request=request)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

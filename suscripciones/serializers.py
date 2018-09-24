from rest_framework import serializers
from .models import *


class SuscripcionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Suscripcion
        fields = ('id', 'usuario', 'lugar', 'fecha_suscripcion', 'notificaciones')


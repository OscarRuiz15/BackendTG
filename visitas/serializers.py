from rest_framework import serializers
from .models import *


class VisitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visita
        fields = ('id', 'usuario', 'lugar', 'fecha_visita', 'hora_visita')
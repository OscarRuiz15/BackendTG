from rest_framework import serializers
from .models import *

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = (
        'id', 'nombre', 'descripcion', 'lugar', 'comentario', 'direccion', 'foto', 'calificacion', 'tipo', 'fecha_inicio',
        'fecha_fin', 'hora_inicio', 'hora_fin', 'finalizado')

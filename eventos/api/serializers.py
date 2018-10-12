from rest_framework import serializers
from eventos.models import Evento
from comentarios.api.serializers import ComentarioSerializer
from drf_writable_nested import WritableNestedModelSerializer


class EventoSerializer(WritableNestedModelSerializer):
    comentario = ComentarioSerializer(many=True)

    class Meta:
        model = Evento
        fields = ['id',
                  'nombre',
                  'descripcion',
                  'lugar',
                  'comentario',
                  'direccion',
                  'foto',
                  'calificacion',
                  'tipo',
                  'fecha_inicio',
                  'fecha_fin',
                  'hora_inicio',
                  'hora_fin',
                  'finalizado',
                  ]

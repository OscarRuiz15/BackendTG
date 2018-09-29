from rest_framework import serializers
from eventos.models import Evento


class EventoSerializer(serializers.HyperlinkedModelSerializer):
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
                  'fecha_hora_inicio',
                  'fecha_hora_fin',
                  'dia_inicio',
                  'mes_inicio',
                  'finalizado',
                  'dia_semana',
                  ]

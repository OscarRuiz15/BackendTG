from rest_framework import serializers
from comentarios.models import Comentario


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id',
                  'mensaje',
                  'usuario',
                  'fecha',
                  'hora',
                  'calificacion'
                  ]

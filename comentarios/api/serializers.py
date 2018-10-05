from rest_framework import serializers
from comentarios.models import Comentario
from usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['id',
                  'nombre',
                  'foto',
                  ]


class ComentarioSerializer(serializers.ModelSerializer):

    usuario = UsuarioSerializer()

    class Meta:
        model = Comentario
        fields = ['id',
                  'mensaje',
                  'usuario',
                  'fecha',
                  'hora',
                  'calificacion'
                  ]

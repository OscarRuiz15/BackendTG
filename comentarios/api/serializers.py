from rest_framework import serializers
from comentarios.models import Comentario
from usuarios.api.serializers import UsuarioSerializer
from usuarios.models import Usuario


class ComentarioSerializer(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(
        read_only=True,
        slug_field='nombre',
    )

    class Meta:
        model = Comentario
        fields = ['id',
                  'mensaje',
                  'usuario',
                  'fecha',
                  'hora',
                  'calificacion'
                  ]

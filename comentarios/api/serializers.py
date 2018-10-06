from rest_framework import serializers
from comentarios.models import Comentario
from usuarios.models import Usuario
from drf_writable_nested import WritableNestedModelSerializer


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id',
                  'nombre',
                  'foto',
                  ]


class ComentarioSerializer(WritableNestedModelSerializer):
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

        def create(self, validated_data):
            user_data = validated_data.pop('usuario')
            user = UsuarioSerializer.create(UsuarioSerializer(), validated_data=user_data)
            comentario, created = Comentario.objects.update_or_create(usuario=user,
                                                                      mensaje=validated_data.pop('mensaje'),
                                                                      fecha=validated_data.pop('fecha'),
                                                                      hora=validated_data.pop('hora'),
                                                                      calificacion=validated_data.pop('calificacion'))
            return comentario

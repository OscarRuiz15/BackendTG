from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from opiniones.models import Opinion
from usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id',
                  'nombre',
                  'foto',
                  ]

class OpinionSerializer(WritableNestedModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Opinion
        fields = ['id',
                  'usuario',
                  'lugar',
                  'like'
                  ]

        def create(self, validated_data):
            user_data = validated_data.pop('usuario')
            user = UsuarioSerializer.create(UsuarioSerializer(), validated_data=user_data)
            opinion, created = Opinion.objects.update_or_create(usuario=user,
                                                                lugar=validated_data.pop('lugar'),
                                                                like=validated_data.pop('like'))
            return opinion

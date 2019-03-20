from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from preferencias.models import Preferencia
from usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id',
                  'nombre',
                  'foto',
                  ]

class PreferenciasSerializer(WritableNestedModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Preferencia
        fields = ['id',
                  'usuario',
                  'tags'
                  ]

        def create(self, validated_data):
            user_data = validated_data.pop('usuario')
            user = UsuarioSerializer.create(UsuarioSerializer(), validated_data=user_data)
            preferencia, created = Preferencia.objects.update_or_create(usuario=user,
                                                                      tags=validated_data.pop('tags'))
            return preferencia

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from suscripciones.models import Suscripcion
from usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id',
                  'nombre',
                  'foto',
                  ]

class SuscripcionSerializer(WritableNestedModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Suscripcion
        fields = ['id',
                  'usuario',
                  'lugar',
                  'fecha_suscripcion',
                  'hora_suscripcion',
                  'notificaciones'
                  ]

        def create(self, validated_data):
            user_data = validated_data.pop('usuario')
            user = UsuarioSerializer.create(UsuarioSerializer(), validated_data=user_data)
            suscripcion, created = Suscripcion.objects.update_or_create(usuario=user,
                                                                      lugar=validated_data.pop('lugar'),
                                                                      fecha_suscripcion=validated_data.pop('fecha_suscripcion'),
                                                                      hora_suscripcion=validated_data.pop('hora_suscripcion'),
                                                                      notificaciones=validated_data.pop('notificaciones'))
            return suscripcion
        # depth = 1

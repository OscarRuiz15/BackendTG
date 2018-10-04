from rest_framework import serializers
from suscripciones.models import Suscripcion
from lugares.models import Lugar


class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = ['id',
                  'nombre',
                  'descripcion',
                  'foto',
                  'calificacion',
                  'direccion',
                  'municipio'
                  ]


class SuscripcionSerializer(serializers.ModelSerializer):
    lugar = LugarSerializer()

    class Meta:
        model = Suscripcion
        fields = ['id',
                  'usuario',
                  'lugar',
                  'fecha_suscripcion',
                  'hora_suscripcion',
                  'notificaciones'
                  ]

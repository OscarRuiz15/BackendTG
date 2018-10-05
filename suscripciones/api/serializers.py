from rest_framework import serializers

from lugares.api.serializers import LugarSerializer
from suscripciones.models import Suscripcion


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
        #depth = 1
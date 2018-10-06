from drf_writable_nested import WritableNestedModelSerializer

from lugares.api.serializers import LugarSerializer
from suscripciones.models import Suscripcion


class SuscripcionSerializer(WritableNestedModelSerializer):
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
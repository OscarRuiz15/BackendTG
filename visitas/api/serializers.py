from drf_writable_nested import WritableNestedModelSerializer
from visitas.models import Visita


class VisitaSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Visita
        fields = ['id',
                  'usuario',
                  'lugar',
                  'fecha_visita',
                  'hora_visita',
                  ]

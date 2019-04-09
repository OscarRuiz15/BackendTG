from drf_writable_nested import WritableNestedModelSerializer
from preferencias.models import Preferencia

class PreferenciasSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Preferencia
        fields = ['id',
                  'usuario',
                  'tags'
                  ]

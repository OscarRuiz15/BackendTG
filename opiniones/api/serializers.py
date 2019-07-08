from drf_writable_nested import WritableNestedModelSerializer
from opiniones.models import Opinion

class OpinionSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Opinion
        fields = ['id',
                  'usuario',
                  'lugar',
                  'like',
                  'valor'
                  ]


from drf_writable_nested import WritableNestedModelSerializer
from ratings.models import Rating


class RatingSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Rating
        fields = ['id',
                  'usuario',
                  'lugar',
        ]


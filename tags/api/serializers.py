from rest_framework import serializers
from tags.models import Tag


class TagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id',
                  'nombre',
                  ]

from rest_framework import serializers
from .models import *

class OpinionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opinion
        fields = ('id', 'usuario', 'lugar', 'like')


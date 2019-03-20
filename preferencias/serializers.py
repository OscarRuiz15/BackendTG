from rest_framework import serializers
from .models import *


class PreferenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Preferencia
        fields = ('id', 'usuario', 'tags')


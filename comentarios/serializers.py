from rest_framework import serializers
from .models import *

class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'mensaje', 'usuario', 'fecha', 'calificacion')


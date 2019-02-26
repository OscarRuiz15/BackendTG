from rest_framework import serializers
from .models import *

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre','descripcion', 'foto')


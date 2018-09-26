from rest_framework import serializers
from categorias.models import Categoria


class CategoriasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id',
                  'nombre',
                  'descripcion',
                  'foto']

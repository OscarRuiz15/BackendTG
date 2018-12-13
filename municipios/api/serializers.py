from rest_framework import serializers
from municipios.models import Municipio


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = [
            'codigo',
            'nombre',
            'departamento'
        ]
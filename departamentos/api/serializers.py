from rest_framework import serializers
from departamentos.models import Departamento


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = [
            'codigo',
            'nombre',
        ]
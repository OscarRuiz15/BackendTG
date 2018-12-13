from rest_framework import serializers

from departamentos.api.serializers import DepartamentoSerializer
from municipios.api.serializers import MunicipioSerializer
from usuarios.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    municipio = MunicipioSerializer()
    departamento = DepartamentoSerializer()

    class Meta:
        model = Usuario
        fields = ['id',
                  'uid',
                  'nombre',
                  'email',
                  'foto',
                  'fecha_nacimiento',
                  'telefono',
                  'genero'
                  'telefono',
                  'departamento',
                  'municipio'
                  ]

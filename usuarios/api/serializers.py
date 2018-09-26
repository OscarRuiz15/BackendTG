from rest_framework import serializers
from usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id',
                  'nombre',
                  'email',
                  'foto',
                  'fecha_nacimiento',
                  'telefono'
        ]
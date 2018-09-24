from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombre','email','foto','fecha_nacimiento','telefono')

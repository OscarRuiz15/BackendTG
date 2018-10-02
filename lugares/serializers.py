from rest_framework import serializers
from .models import *

class LugarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lugar
        fields = (
        'id', 'nombre', 'descripcion', 'foto', 'producto', 'calificacion', 'tag', 'email', 'sitio_web', 'telefono',
        'redes', 'comentario', 'direccion', 'hora_abierto', 'hora_cerrado', 'dias_servicio', 'latitud', 'longitud',
        'municipio', 'categoria', 'propietario')

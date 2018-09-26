from rest_framework import serializers
from solicitudes.models import Solicitud


class SolicitudSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['id',
                  'usuario',
                  'nombre_lugar',
                  'direccion',
                  'telefono',
                  'email',
                  'informacion',
                  'nit',
                  'aceptado'
                  ]
from drf_writable_nested import WritableNestedModelSerializer

from solicitudes.models import Solicitud


class SolicitudSerializer(WritableNestedModelSerializer):
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
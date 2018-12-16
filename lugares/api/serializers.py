from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from comentarios.api.serializers import ComentarioSerializer
from departamentos.api.serializers import DepartamentoSerializer
from lugares.models import Lugar
from municipios.api.serializers import MunicipioSerializer
from productos.api.serializers import ProductoSerializer
from tags.api.serializers import TagsSerializer


class LugarSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    producto = ProductoSerializer(many=True)
    tag = TagsSerializer(many=True)
    comentario = ComentarioSerializer(many=True)
    departamento = DepartamentoSerializer(read_only=True)
    municipio = MunicipioSerializer(read_only=True)

    class Meta:
        model = Lugar
        fields = ['id',
                  'nombre',
                  'descripcion',
                  'foto',
                  'producto',
                  'calificacion',
                  'tag',
                  'email',
                  'sitio_web',
                  'telefono',
                  'redes',
                  'comentario',
                  'direccion',
                  'hora_abierto',
                  'hora_cerrado',
                  'dias_servicio',
                  'latitud',
                  'longitud',
                  'municipio',
                  'categoria',
                  'propietario',
                  'fecha_creacion',
                  'departamento',
                  'municipio'
                  ]

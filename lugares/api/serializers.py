from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from comentarios.api.serializers import ComentarioSerializer
from lugares.models import Lugar
from lugares.models import RecomendacionLugares
from tags.api.serializers import TagsSerializer


class LugarSerializer(serializers.ModelSerializer):
    tag = TagsSerializer(many=True)
    comentario = ComentarioSerializer(many=True)

    class Meta:
        model = Lugar
        fields = ['id',
                  'nombre',
                  'descripcion',
                  'foto',
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

class RecomendacionLugarSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecomendacionLugares
        fields = ['valor',
                  'lugar',
                  'usuario']

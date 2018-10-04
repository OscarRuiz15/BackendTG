from rest_framework import serializers
from lugares.models import Lugar
from productos.api.serializers import ProductoSerializer
from productos.models import Producto
from tags.api.serializers import TagsSerializer
from tags.models import Tag
from comentarios.api.serializers import ComentarioSerializer
from comentarios.models import Comentario


class LugarSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(many=True)
    tag = TagsSerializer(many=True)
    comentario = ComentarioSerializer(many=True)

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
        ]

        def create(self, validated_data):
            productos_data = validated_data.pop('producto')
            lugar = Lugar.objects.create(**validated_data)
            for producto_data in productos_data:
                Producto.objects.create(lugar=lugar, **producto_data)
            return lugar

        def create(self, validated_data):
            tags_data = validated_data.pop('tag')
            lugar = Lugar.objects.create(**validated_data)
            for tag_data in tags_data:
                Producto.objects.create(lugar=lugar, **tag_data)
            return lugar

        def create(self, validated_data):
            comentarios_data = validated_data.pop('comentario')
            lugar = Lugar.objects.create(**validated_data)
            for comentario_data in comentarios_data:
                Producto.objects.create(lugar=lugar, **comentario_data)
            return lugar


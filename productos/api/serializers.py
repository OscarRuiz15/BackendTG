from rest_framework import serializers
from productos.models import Producto


def push_notify(nombre_lugar, nombre_producto, id_lugar):
    from pusher_push_notifications import PushNotifications

    pn_client = PushNotifications(
        instance_id='150ee5d4-aa83-42f8-9c65-fe6ab983f0ca',
        secret_key='FA39827AAB5E866F8084A0FD034F5CB59D987D566D35ED66BBEEA1564D561E93',
    )
    message = nombre_lugar + ' ha agregado ' + nombre_producto + ' a sus productos'
    interest = str(id_lugar)
    response = pn_client.publish(
        interests=[interest],
        publish_body={'apns': {'aps': {'alert': 'Hello!'}},
                      'fcm': {'notification': {'title': 'Nuevo Evento', 'body': message}}}
    )

    print(response['publishId'])


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id',
                  'nombre',
                  'descripcion',
                  'precio',
                  'foto',
                  'lugar',
                  ]

    def create(self, validated_data):
        nombre = validated_data.get('nombre')
        descripcion = validated_data.get('descripcion')
        precio = validated_data.get('precio')
        foto = validated_data.get('foto')
        lugar = validated_data.get('lugar')
        producto = Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            foto=foto,
            lugar=lugar
        )
        push_notify(lugar.nombre, nombre, lugar.id)
        return producto

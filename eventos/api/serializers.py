from rest_framework import serializers
from eventos.models import Evento
from comentarios.api.serializers import ComentarioSerializer
from drf_writable_nested import WritableNestedModelSerializer


class EventoSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Evento
        fields = ['id',
                  'nombre',
                  'descripcion',
                  'lugar',
                  'comentario',
                  'direccion',
                  'foto',
                  'calificacion',
                  'tipo',
                  'fecha_inicio',
                  'fecha_fin',
                  'hora_inicio',
                  'hora_fin',
                  'finalizado',
                  ]

    comentario = ComentarioSerializer(many=True)

    def create(self, validated_data):
        nombre = validated_data.get('nombre')
        descripcion = validated_data.get('descripcion')
        lugar = validated_data.get('lugar')
        comentario = validated_data.get('comentario')
        direccion = validated_data.get('direccion')
        foto = validated_data.get('foto')
        calificacion = validated_data.get('calificacion')
        tipo = validated_data.get('tipo')
        fecha_inicio = validated_data.get('fecha_inicio')
        fecha_fin = validated_data.get('fecha_fin')
        hora_inicio = validated_data.get('hora_inicio')
        hora_fin = validated_data.get('hora_fin')
        finalizado = validated_data.get('finalizado')
        self.push_notify(nombre_lugar=lugar.nombre, nombre_evento=nombre, id_lugar=lugar.id)
        evento = Evento.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            lugar=lugar,
            direccion=direccion,
            foto=foto,
            calificacion=calificacion,
            tipo=tipo,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            finalizado=finalizado,
        )
        evento.comentario.set(comentario)
        return evento

    def push_notify(self, nombre_lugar, nombre_evento, id_lugar):
        from pusher_push_notifications import PushNotifications

        pn_client = PushNotifications(
            instance_id='150ee5d4-aa83-42f8-9c65-fe6ab983f0ca',
            secret_key='FA39827AAB5E866F8084A0FD034F5CB59D987D566D35ED66BBEEA1564D561E93',
        )
        message = nombre_lugar + ' ha creado el evento ' + nombre_evento
        interest = str(id_lugar)
        response = pn_client.publish(
            interests=[interest],
            publish_body={'apns': {'aps': {'alert': 'Hello!'}},
                          'fcm': {'notification': {'title': 'Nuevo Evento', 'body': message}}}
        )

        print(response['publishId'])

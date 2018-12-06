from rest_framework import generics,mixins
from eventos.models import Evento
from .serializers import EventoSerializer
from django.db.models import Q

class EventoView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = EventoSerializer

    def get_queryset(self):
        return Evento.objects.all()


class EventoListView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = EventoSerializer

    def get_queryset(self):
        qs = Evento.objects.all()
        query = self.request.GET.get("lugar")
        if query is not None:
            qs = qs.filter(Q(lugar__id=query)).distinct()
        else:
            query = self.request.GET.get("nombre")
            if query is not None:
                qs = qs.filter(Q(nombre__icontains=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        self.push_notify()
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def push_notify(self):
        from pusher_push_notifications import PushNotifications

        pn_client = PushNotifications(
            instance_id='150ee5d4-aa83-42f8-9c65-fe6ab983f0ca',
            secret_key='FA39827AAB5E866F8084A0FD034F5CB59D987D566D35ED66BBEEA1564D561E93',
        )
        response = pn_client.publish(
            interests=['hello'],
            publish_body={'apns': {'aps': {'alert': 'Hello!'}},
                          'fcm': {'notification': {'title': 'Hello', 'body': 'Hello, World!'}}}
        )

        print(response['publishId'])




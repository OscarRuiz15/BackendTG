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
        return Evento.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

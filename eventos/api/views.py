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
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)






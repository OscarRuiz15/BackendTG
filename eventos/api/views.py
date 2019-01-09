from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer

from BackendTG.permisos import AuthFirebaseUser
from eventos.models import Evento
from .serializers import EventoSerializer


class EventoView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = EventoSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Evento.objects.all()


class EventoListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = EventoSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

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


class EventoSuscrito(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = EventoSerializer
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        qs = Evento.objects.all()
        query = self.request.GET.get("usuario")
        if query is not None:
            qs = qs.filter(Q(lugar__suscripcion__usuario__uid=query))
        return qs

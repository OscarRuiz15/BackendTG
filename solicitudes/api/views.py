from rest_framework import generics,mixins
from .serializers import SolicitudSerializer
from solicitudes.models import Solicitud
from django.db.models import Q


class SolicitudesView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = SolicitudSerializer

    def get_queryset(self):
        return Solicitud.objects.all()


class SolictidudesListView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = SolicitudSerializer

    def get_queryset(self):
        return Solicitud.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


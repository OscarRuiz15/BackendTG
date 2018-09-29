# generic
from django.db.models import Q
from rest_framework import generics, mixins
from visitas.models import Visita
from .serializers import VisitaSerializer

class VisitasView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = VisitaSerializer

    def get_queryset(self):
        return Visita.objects.all()


class VisitasListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = VisitaSerializer

    def get_queryset(self):
        return Visita.objects.all()

    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)


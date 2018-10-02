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
        qs = Visita.objects.all()
        query = self.request.GET.get("usuario")
        if query is not None:
            qs = qs.filter(Q(usuario__uid=query)).distinct()
        else:
            query = self.request.GET.get("lugar")
            if query is not None:
                qs = qs.filter(Q(lugar__id=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)


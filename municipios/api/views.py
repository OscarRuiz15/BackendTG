from rest_framework import generics, viewsets, mixins
from django.db.models import Q
from municipios.models import Municipio
from .serializers import MunicipioSerializer


# Consulta por Id
class MunicipioViewId(generics.RetrieveUpdateAPIView):
    lookup_field = 'codigo'
    serializer_class = MunicipioSerializer

    def get_queryset(self):
        return Municipio.objects.all()


# Consulta por Nombre
class MunicipioView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'codigo'
    serializer_class = MunicipioSerializer

    def get_queryset(self):
        qs = Municipio.objects.all()
        query = self.request.GET.get("departamento")
        if query is not None:
            qs = qs.filter(Q(departamento__nombre=query))
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

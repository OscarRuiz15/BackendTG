from rest_framework import generics, viewsets, mixins
from departamentos.models import Departamento
from .serializers import DepartamentoSerializer


# Consulta por Id
class DepartamentoViewId(generics.RetrieveUpdateAPIView):
    lookup_field = 'codigo'
    serializer_class = DepartamentoSerializer

    def get_queryset(self):
        return Departamento.objects.all()


# Consulta por Nombre
class DepartamentoView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'codigo'
    serializer_class = DepartamentoSerializer

    def get_queryset(self):
        qs = Departamento.objects.all()
        query = self.request.GET.get("nombre")

        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

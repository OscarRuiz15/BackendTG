from django.db.models import Q
from rest_framework import generics, viewsets, mixins
from productos.models import Producto
from .serializers import ProductoSerializer

#Consulta por Id
class ProductoViewId(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ProductoSerializer

    def get_queryset(self):
        return Producto.objects.all()

#Consulta por Nombre
class ProductoView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ProductoSerializer

    def get_queryset(self):
        qs=Producto.objects.all()
        query=self.request.GET.get("nombre")
        if query is not None:
            qs=qs.filter(Q(nombre__icontains=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args,**kwargs)
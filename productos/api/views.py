from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer

from BackendTG.permisos import AuthFirebaseUser
from productos.models import Producto
from .serializers import ProductoSerializer


class ProductoViewId(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ProductoSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Producto.objects.all()


class ProductoView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ProductoSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        qs = Producto.objects.all()
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

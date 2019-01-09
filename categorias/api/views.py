import firebase_admin
from firebase_admin import credentials, auth
from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer

from BackendTG.permisos import AuthFirebaseUser
from categorias.models import Categoria
from .serializers import CategoriasSerializer


class CategoriasView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = CategoriasSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Categoria.objects.all()


class CategoriasListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = CategoriasSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Categoria.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

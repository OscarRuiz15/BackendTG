from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer

from BackendTG.permisos import AuthFirebaseUser
from comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ComentarioSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Comentario.objects.all()


class ComentarioListView(generics.ListAPIView, mixins.CreateModelMixin):
    lookup_field = 'id'
    serializer_class = ComentarioSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Comentario.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

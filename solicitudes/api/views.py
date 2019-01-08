from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer

from BackendTG.permisos import AuthFirebaseUser
from solicitudes.models import Solicitud
from .serializers import SolicitudSerializer


class SolicitudesView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = SolicitudSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Solicitud.objects.all()


class SolictidudesListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = SolicitudSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Solicitud.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer

from django.db.models import Q
from BackendTG.permisos import AuthFirebaseUser
from solicitudes.models import Solicitud
from .serializers import SolicitudSerializer


class SolicitudesView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = SolicitudSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Solicitud.objects.all()


class SolicitudesListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = SolicitudSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        qs = Solicitud.objects.all()
        query = self.request.GET.get("usuario")
        if query is not None:
            qs = qs.filter(Q(usuario__uid__exact=query))
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




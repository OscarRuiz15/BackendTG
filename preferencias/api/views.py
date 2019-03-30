from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer

from BackendTG.permisos import AuthFirebaseUser
from preferencias.models import Preferencia
from .serializers import PreferenciasSerializer


class PreferenciasView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = PreferenciasSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Preferencia.objects.all()


class PreferenciasListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PreferenciasSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        qs = Preferencia.objects.all()
        query = self.request.GET.get("usuario")
        if query is not None:
            qs = qs.filter(Q(usuario__uid__exact=query))
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

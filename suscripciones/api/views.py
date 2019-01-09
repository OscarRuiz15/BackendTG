from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from BackendTG.permisos import AuthFirebaseUser
from suscripciones.models import Suscripcion
from .serializers import SuscripcionSerializer


class SuscripcionView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = SuscripcionSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Suscripcion.objects.all()


class SuscripcionListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = SuscripcionSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        qs = Suscripcion.objects.all()
        query = self.request.GET.get("usuario")
        if query is not None:
            qs = qs.filter(Q(usuario__uid=query)).distinct()
        else:
            query = self.request.GET.get("lugar")
            if query is not None:
                qs = qs.filter(Q(lugar__id=query)).distinct()
            else:
                query = self.request.GET.get("nombre")
                query2 = self.request.GET.get("uid")
                if query is not None:
                    qs = qs.filter(Q(lugar__nombre__icontains=query)).distinct() & qs.filter(
                        Q(usuario__uid=query2)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SuscripcionUsuarioCount(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get(self, request, format=None):
        qs = Suscripcion.objects.all()
        query = self.request.GET.get("usuario")
        if query is not None:
            qs = qs.filter(Q(usuario__uid__exact=query)).distinct()
        contador = qs.count()
        content = {'user_count': contador}
        return Response(content)

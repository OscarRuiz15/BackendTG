# generic
from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from BackendTG.permisos import AuthFirebaseUser
from visitas.models import Visita
from .serializers import VisitaSerializer


class VisitasView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = VisitaSerializer
    renderer_classes = (JSONRenderer,)
    #permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Visita.objects.all()


class VisitasListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = VisitaSerializer
    renderer_classes = (JSONRenderer,)
    #permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        qs = Visita.objects.all()
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


class VisitasUsuarioCount(APIView):
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        qs = Visita.objects.all()
        query = self.request.GET.get("usuario")
        if query is not None:
            qs = qs.filter(Q(usuario__uid=query)).distinct()
        contador = qs.count()
        content = {'user_count': contador}
        return Response(content)

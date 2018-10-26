from django.db.models import Q
from rest_framework import generics, viewsets, mixins
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from lugares.models import Lugar
from .serializers import LugarSerializer


class LugaresView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer

    def get_queryset(self):
        return Lugar.objects.all()


class LugaresListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer

    def get_queryset(self):
        qs = Lugar.objects.all()
        query = self.request.GET.get("categoria")
        if query is not None:
            qs = qs.filter(Q(categoria__id=query)).distinct()
        else:
            query = self.request.GET.get("lugar")
            if query is not None:
                qs = qs.filter(Q(id=query)).distinct()
            else:
                query = self.request.GET.get("nombre")
                if query is not None:
                    qs = qs.filter(Q(nombre__icontains=query)).distinct()
                else:
                    query = self.request.GET.get("propietario")
                    if query is not None:
                        qs = qs.filter(Q(propietario__uid=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LugaresUsuarioCount(APIView):
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        qs = Lugar.objects.all()
        query = self.request.GET.get("usuario")
        if query is not None:
            qs = qs.filter(Q(propietario__uid=query)).distinct()
        contador = qs.count()
        content = {'user_count': contador}
        return Response(content)

from django.db.models import Q
from rest_framework import generics, viewsets, mixins
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
                qs = qs.filter(Q(lugar__id=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args,**kwargs)
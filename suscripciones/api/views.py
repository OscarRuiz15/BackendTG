from rest_framework import generics,mixins
from .serializers import SuscripcionSerializer
from suscripciones.models import Suscripcion
from django.db.models import Q


class SuscripcionView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = SuscripcionSerializer

    def get_queryset(self):
        return Suscripcion.objects.all()


class SuscripcionListView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = SuscripcionSerializer

    def get_queryset(self):
        qs=Suscripcion.objects.all()
        query=self.request.GET.get("usuario")
        if query is not None:
            qs=qs.filter(Q(usuario__uid=query)).distinct()
        else:
            query = self.request.GET.get("lugar")
            if query is not None:
                qs = qs.filter(Q(lugar__id=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



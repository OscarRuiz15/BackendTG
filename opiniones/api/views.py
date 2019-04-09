from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer

from BackendTG.permisos import AuthFirebaseUser
from opiniones.models import Opinion
from .serializers import OpinionSerializer


class OpinionView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = OpinionSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Opinion.objects.all()


class OpinionListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = OpinionSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        qs = Opinion.objects.all()
        query = self.request.GET.get("usuario")
        if query is not None:
            qs = qs.filter(Q(usuario__uid__exact=query))
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

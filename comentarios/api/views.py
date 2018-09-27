from rest_framework import generics,mixins
from .serializers import ComentarioSerializer
from comentarios.models import Comentario
from django.db.models import Q


class ComentarioView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        return Comentario.objects.all()


class ComentarioListView(generics.ListAPIView,mixins.CreateModelMixin):
    lookup_field = 'id'
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        return Comentario.objects.all()

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
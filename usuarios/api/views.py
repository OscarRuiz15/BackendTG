# generic
from django.db.models import Q
from rest_framework import generics, mixins
from usuarios.models import Usuario
from .serializers import UsuarioSerializer



class UsuariosView(generics.RetrieveUpdateAPIView):
    lookup_field = 'uid'  # id url(?P<id>d+)
    serializer_class = UsuarioSerializer
    #queryset = Usuario.objects.all()

    def get_queryset(self):
        return Usuario.objects.all()



class UsuariosListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'  # id url(?P<id>d+)
    serializer_class = UsuarioSerializer

    # queryset = Usuario.objects.all()

    def get_queryset(self):
        qs = Usuario.objects.all()
        query= self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(nombre__icontains=query)).distinct()
        return qs


    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


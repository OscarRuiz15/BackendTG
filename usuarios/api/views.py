# generic

from rest_framework import generics
from usuarios.models import Usuario
from .serializers import UsuarioSerializer



class UsuariosView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'  # id url(?P<id>d+)
    serializer_class = UsuarioSerializer
    #queryset = Usuario.objects.all()

    def get_queryset(self):
        return Usuario.objects.all()

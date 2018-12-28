# generic
import firebase_admin
from django.db.models import Q
from firebase_admin import credentials, auth
from rest_framework import generics, mixins
from usuarios.models import Usuario
from .serializers import UsuarioSerializer

cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)

class UsuariosView(generics.RetrieveUpdateAPIView):
    lookup_field = 'uid'  # id url(?P<id>d+)
    serializer_class = UsuarioSerializer
    #queryset = Usuario.objects.all()

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return Usuario.objects.all()
        except:
            return None


class UsuariosListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'  # id url(?P<id>d+)
    serializer_class = UsuarioSerializer

    # queryset = Usuario.objects.all()

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            qs = Usuario.objects.all()
            query = self.request.GET.get("q")
            if query is not None:
                qs = qs.filter(Q(nombre__icontains=query)).distinct()
            return qs
        except:
            return None

    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return self.update(request, *args, **kwargs)
        except:
            return None



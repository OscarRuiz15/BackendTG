import firebase_admin
from firebase_admin import credentials, auth
from rest_framework import generics, mixins
from .serializers import ComentarioSerializer
from comentarios.models import Comentario
from django.db.models import Q

cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)


class ComentarioView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return Comentario.objects.all()
        except:
            return None


class ComentarioListView(generics.ListAPIView, mixins.CreateModelMixin):
    lookup_field = 'id'
    serializer_class = ComentarioSerializer

    def get_queryset(self):

        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return Comentario.objects.all()
        except:
            return None

    def post(self, request, *args, **kwargs):

        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return self.create(request, *args, **kwargs)
        except:
            return None

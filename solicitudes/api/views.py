import firebase_admin
from firebase_admin import credentials, auth
from rest_framework import generics,mixins
from .serializers import SolicitudSerializer
from solicitudes.models import Solicitud
from django.db.models import Q


cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)

class SolicitudesView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = SolicitudSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return Solicitud.objects.all()
        except:
            return None




class SolictidudesListView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = SolicitudSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return Solicitud.objects.all()
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



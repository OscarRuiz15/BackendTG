import firebase_admin
from firebase_admin import credentials, auth
from rest_framework import generics,mixins
from eventos.models import Evento
from lugares.models import Lugar
from suscripciones.models import Suscripcion
from usuarios.models import Usuario
from .serializers import EventoSerializer
from django.db.models import Q

cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)

class EventoView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = EventoSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return Evento.objects.all()
        except:
            return None



class EventoListView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = EventoSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)

            qs = Evento.objects.all()
            query = self.request.GET.get("lugar")
            if query is not None:
                qs = qs.filter(Q(lugar__id=query)).distinct()
            else:
                query = self.request.GET.get("nombre")
                if query is not None:
                    qs = qs.filter(Q(nombre__icontains=query)).distinct()
            return qs
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



class EventoSuscrito(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = EventoSerializer

    def get_queryset(self):

        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            qs = Evento.objects.all()
            query = self.request.GET.get("usuario")
            if query is not None:
                qs = qs.filter(Q(lugar__suscripcion__usuario__uid=query))
            return qs
        except:
            return None





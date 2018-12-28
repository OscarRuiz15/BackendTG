import firebase_admin
from firebase_admin import credentials, auth
from rest_framework import generics,mixins
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SuscripcionSerializer
from suscripciones.models import Suscripcion
from django.db.models import Q

cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)

class SuscripcionView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = SuscripcionSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return Suscripcion.objects.all()
        except:
            return None



class SuscripcionListView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = SuscripcionSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            qs=Suscripcion.objects.all()
            query=self.request.GET.get("usuario")
            if query is not None:
                qs=qs.filter(Q(usuario__uid=query)).distinct()
            else:
                query = self.request.GET.get("lugar")
                if query is not None:
                    qs = qs.filter(Q(lugar__id=query)).distinct()
                else:
                    query = self.request.GET.get("nombre")
                    query2 = self.request.GET.get("uid")
                    if query is not None:
                        qs = qs.filter(Q(lugar__nombre__icontains=query)).distinct() & qs.filter(Q(usuario__uid=query2)).distinct()
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





class SuscripcionUsuarioCount(APIView):
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        try:
            qs = Suscripcion.objects.all()
            query = self.request.GET.get("usuario")
            if query is not None:
                qs = qs.filter(Q(usuario__uid__exact=query)).distinct()
            contador = qs.count()
            content = {'user_count': contador}
            return Response(content)
        except:
            return None


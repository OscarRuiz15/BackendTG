# generic
import firebase_admin
from django.db.models import Q
from firebase_admin import credentials, auth
from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from visitas.models import Visita
from .serializers import VisitaSerializer

cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)


class VisitasView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = VisitaSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return Visita.objects.all()
        except:
            return None


class VisitasListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = VisitaSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            qs = Visita.objects.all()
            query = self.request.GET.get("usuario")
            if query is not None:
                qs = qs.filter(Q(usuario__uid=query)).distinct()
            else:
                query = self.request.GET.get("lugar")
                if query is not None:
                    qs = qs.filter(Q(lugar__id=query)).distinct()
                else:
                    query = self.request.GET.get("nombre")
                    query2 = self.request.GET.get("uid")
                    if query is not None:
                        qs = qs.filter(Q(lugar__nombre__icontains=query)).distinct() & qs.filter(
                            Q(usuario__uid=query2)).distinct()
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


class VisitasUsuarioCount(APIView):
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            qs = Visita.objects.all()
            query = self.request.GET.get("usuario")
            if query is not None:
                qs = qs.filter(Q(usuario__uid=query)).distinct()
            contador = qs.count()
            content = {'user_count': contador}
            return Response(content)
        except:
            return None


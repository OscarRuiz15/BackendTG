import firebase_admin
from firebase_admin import credentials, auth
from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer

from categorias.models import Categoria
from .serializers import CategoriasSerializer


class CategoriasView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class =  CategoriasSerializer
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return Categoria.objects.all()
        except:
            return None




class CategoriasListView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = CategoriasSerializer
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return Categoria.objects.all()
        except:
            return None

    def post(self,request,*args,**kwargs):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return self.create(request, *args, **kwargs)
        except:
            return None
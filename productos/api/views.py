import firebase_admin
from django.db.models import Q
from firebase_admin import credentials, auth
from rest_framework import generics, viewsets, mixins
from productos.models import Producto
from .serializers import ProductoSerializer

cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)

#Consulta por Id
class ProductoViewId(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ProductoSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return Producto.objects.all()
        except:
            return None


#Consulta por Nombre
class ProductoView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ProductoSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            qs=Producto.objects.all()
            query=self.request.GET.get("nombre")
            if query is not None:
                qs=qs.filter(Q(nombre__icontains=query)).distinct()
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


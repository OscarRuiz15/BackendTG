import firebase_admin
from firebase_admin import credentials, auth
from rest_framework import generics,mixins
from tags.models import Tag
from .serializers import TagsSerializer
from django.db.models import Q

cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)

class TagsView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = TagsSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return Tag.objects.all()
        except:
            return None





class TagsListView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = TagsSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            qs = Tag.objects.all()
            query = self.request.GET.get("q")
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


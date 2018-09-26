from rest_framework import generics,mixins
from tags.models import Tag
from .serializers import TagsSerializer
from django.db.models import Q


class TagsView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = TagsSerializer

    def get_queryset(self):
        return Tag.objects.all()




class TagsListView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = TagsSerializer

    def get_queryset(self):
        qs = Tag.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs= qs.filter(Q(nombre__icontains=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

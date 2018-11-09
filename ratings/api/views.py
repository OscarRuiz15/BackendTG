from django.db.models import Q
from rest_framework import generics, viewsets, mixins
from ratings.models import Rating
from .serializers import RatingSerializer


class RatingsView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.all()


class RatingsListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = RatingSerializer

    def get_queryset(self):
        qs=Rating.objects.all()
        query=self.request.GET.get("usuario")
        if query is not None:
            qs=qs.filter(Q(usuario__uid=query)).distinct()
        else:
            query = self.request.GET.get("lugar")
            if query is not None:
                qs = qs.filter(Q(lugar__id=query)).distinct()
        return qs


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


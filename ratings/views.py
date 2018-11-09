from django.shortcuts import render
from rest_framework import viewsets
from ratings.models import Rating
from .serializers import *

# Create your views here.
class RatingViewSite(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

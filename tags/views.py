from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class TagViewSite(viewsets.ModelViewSet):
	queryset=Tag.objects.all()
	serializer_class=TagSerializer

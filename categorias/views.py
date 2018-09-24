from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class CategoriaViewSite(viewsets.ModelViewSet):
	queryset=Categoria.objects.all()
	serializer_class=CategoriaSerializer

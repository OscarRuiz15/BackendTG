from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class ComentarioViewSite(viewsets.ModelViewSet):
	queryset=Comentario.objects.all()
	serializer_class=ComentarioSerializer

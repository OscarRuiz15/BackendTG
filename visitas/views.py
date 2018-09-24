from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class VisitaViewSite(viewsets.ModelViewSet):
	queryset=Visita.objects.all()
	serializer_class=VisitaSerializer
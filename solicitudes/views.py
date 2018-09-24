from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class SolicitudViewSite(viewsets.ModelViewSet):
	queryset=Solicitud.objects.all()
	serializer_class=SolicitudSerializer
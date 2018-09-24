from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class EventoViewSite(viewsets.ModelViewSet):
	queryset=Evento.objects.all()
	serializer_class=EventoSerializer
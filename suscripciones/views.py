from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class SuscripcionViewSite(viewsets.ModelViewSet):
	queryset=Suscripcion.objects.all()
	serializer_class=SuscripcionSerializer

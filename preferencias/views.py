from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *

# Create your views here.
class PreferenciaViewSite(viewsets.ModelViewSet):
	queryset=Preferencia.objects.all()
	serializer_class=PreferenciaSerializer

from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class LugarViewSite(viewsets.ModelViewSet):
	queryset=Lugar.objects.all()
	serializer_class=LugarSerializer

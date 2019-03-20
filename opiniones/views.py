from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *

# Create your views here.
class OpinionViewSite(viewsets.ModelViewSet):
	queryset=Opinion.objects.all()
	serializer_class=OpinionSerializer
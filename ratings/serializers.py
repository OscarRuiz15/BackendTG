from rest_framework import serializers
from .models import *

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','usuario','lugar')
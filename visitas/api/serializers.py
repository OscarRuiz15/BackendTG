from rest_framework import serializers
from visitas.models import Visita


class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = ['id',
                  'usuario',
                  'lugar',
                  ]

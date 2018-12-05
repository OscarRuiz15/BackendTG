import decimal

import numpy as np
from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from lugares.models import Lugar
from .serializers import LugarSerializer


class LugaresView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer

    def get_queryset(self):
        return Lugar.objects.all()

    def put(self, request, *args, **kwargs):
        lugar = self.get_object()
        lista = []
        for comentario in lugar.comentario.all():
            lista.append(comentario.calificacion)
        array = np.array(lista)
        lugar.calificacion = np.mean(array)
        lugar.save()
        lugar.save_base()
        return self.update(request, *args, **kwargs)


class LugaresListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer

    def get_queryset(self):
        qs = Lugar.objects.all()
        query = self.request.GET.get("categoria")
        if query is not None:
            qs = qs.filter(Q(categoria__id=query)).distinct()
        else:
            query = self.request.GET.get("lugar")
            if query is not None:
                qs = qs.filter(Q(id=query)).distinct()
            else:
                query = self.request.GET.get("nombre")
                if query is not None:
                    qs = qs.filter(Q(nombre__icontains=query)).distinct()
                else:
                    query = self.request.GET.get("propietario")
                    if query is not None:
                        qs = qs.filter(Q(propietario__uid=query)).distinct()
                    else:
                        query = self.request.GET.get("nombre")
                        query2 = self.request.GET.get("uid")
                        if query is not None:
                            qs = qs.filter(Q(nombre__icontains=query)).distinct() & qs.filter(
                                Q(propietario__uid=query2)).distinct()

        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LugaresPopulares(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer

    def weighted_rating(self, calificacion, votos, m, C):
        v = votos
        R = calificacion
        # Calculo de la formula dada por la IMDB

        return (decimal.Decimal(v / (v + m)) * R) + (decimal.Decimal(m / (m + v)) * C)

    def get_queryset(self):
        c = 0.0
        m = 0.0
        populares = Lugar.objects.all()
        lista = []
        calificaciones = []
        cantidad = []
        for x in populares:
            for i in x.comentario.all():
                lista.append(i.calificacion)

            array = np.array(lista)
            x.calificacion = np.mean(array)
            calificaciones.append(x.calificacion)
            cantidad.append(x.comentario.count())

            np_calificaciones = np.array(calificaciones)
            np_cantidad = np.array(cantidad)

        c = np.mean(np_calificaciones)
        m = np.quantile(np_cantidad, .9)

        for lugar in populares:
            lugar.calificacion = self.weighted_rating(lugar.calificacion, lugar.comentario.count(), m, c)
            print(lugar.calificacion)


        populares.order_by('calificacion')
        return populares


class LugaresUsuarioCount(APIView):
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        qs = Lugar.objects.all()
        query = self.request.GET.get("usuario")
        if query is not None:
            qs = qs.filter(Q(propietario__uid=query)).distinct()
        contador = qs.count()
        content = {'user_count': contador}
        return Response(content)

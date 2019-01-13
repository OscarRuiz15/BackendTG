import decimal
from datetime import date, timedelta

import numpy as np
from django.db.models import Q
from firebase_admin import auth
from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from BackendTG.permisos import AuthFirebaseUser, IsAdmin
from lugares.models import Lugar
from suscripciones.models import Suscripcion
from visitas.models import Visita
from .serializers import LugarSerializer


##############################################################################################
class LugaresView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Lugar.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


##############################################################################################
class LugaresListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (IsAdmin,)

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


##############################################################################################
class LugaresPopulares(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer
    permission_classes = (AuthFirebaseUser,)

    def weighted_rating(self, calificacion, votos, m, C):
        v = votos
        R = calificacion
        # Calculo de la formula dada por la IMDB

        return (decimal.Decimal(v / (v + m)) * R) + (decimal.Decimal(m / (m + v)) * C)

    def get_queryset(self):
        global np_calificaciones, np_cantidad

        c = 0
        m = 0
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
        print(c)
        m = np.quantile(np_cantidad, .9)

        for lugar in populares:
            lugar.calificacion = self.weighted_rating(lugar.calificacion, lugar.comentario.count(), m, c)
            print(lugar.calificacion)

        populares.order_by('calificacion')
        return populares


##############################################################################################
class LugaresUsuarioCount(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get(self, request, format=None):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)

            qs = Lugar.objects.all()
            query = self.request.GET.get("usuario")
            if query is not None:
                qs = qs.filter(Q(propietario__uid=query)).distinct()
            contador = qs.count()
            content = {'user_count': contador}
            return Response(content)

        except:
            return None


##############################################################################################
class LugaresVisitasCount(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get(self, request, format=None):
        visitas = Visita.objects.all()
        suscripciones = Suscripcion.objects.all()
        query = self.request.GET.get("lugar")
        if query is not None:
            visitas = visitas.filter(Q(lugar__id=query))
            suscripciones = suscripciones.filter(Q(lugar__id=query))
        print(query)
        contador_visitas = visitas.count()
        contador_suscripciones = suscripciones.count()
        content = {'visitas': contador_visitas,
                   'suscripciones': contador_suscripciones
                   }
        return Response(content)


##############################################################################################
class LugaresVisitados(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        qs = Lugar.objects.all()
        query = self.request.GET.get('usuario')
        if query is not None:
            qs = qs.filter((Q(visita__usuario__uid=query))).distinct()
        return qs


##############################################################################################
class LugaresSuscrito(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        qs = Lugar.objects.all()
        query = self.request.GET.get('usuario')
        if query is not None:
            qs = qs.filter((Q(suscripcion__usuario__uid=query)))
        return qs


##############################################################################################
class LugaresNuevos(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        query = self.request.GET.get('dias')
        lugares = []
        for lugar in Lugar.objects.all():
            hoy = date.today()
            diferencia = hoy - lugar.fecha_creacion
            if diferencia <= timedelta(days=int(query)):
                lugares.append(lugar)
        return lugares


##############################################################################################
class LugaresRecomendados(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):

        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import linear_kernel
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

        # Function to convert all strings to lower case and strip names of spaces
        def clean_data(x):
            if isinstance(x, str):
                return str.lower(x.replace(" ", ""))
            else:
                return ''

        lugares = Lugar.objects.all()

        query = self.request.GET.get('lugar')
        descripciones = []
        tags = []
        lugars = []
        for lugar in lugares:
            lugars.append(lugar)
        stop_words = ['una', 'el', 'un', 'la', 'es', 'esta', 'de', 'los', 'las', 'unas', 'unos', 'al', 'del', 'lo',
                      'y',
                      'a', 'somos', 'cuenta', 'con', 'porque', 'ya', 'que', 'mas', 'en', 'para', 'su', 'se', 'ha']

        lugars.sort(key=lambda x: x.id)
        for lugar in lugars:
            descripciones.append(lugar.descripcion)
            palabras = ''
            for tag in lugar.tag.all():
                palabras += clean_data(tag.nombre) + ' '
            tags.append(palabras)

        print(tags)
        tfidf = TfidfVectorizer(stop_words=stop_words)
        tfidf_matrix = tfidf.fit_transform(descripciones)

        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        count = CountVectorizer(stop_words=stop_words)
        count_matrix = count.fit_transform(tags)
        cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

        print(cosine_sim2)

        l = []
        idx = int(query) - 1
        # Quitar cuando se limpie la bd
        if idx >= 2:
            idx = idx - 1
        sim_scores = list(enumerate(cosine_sim[idx]))

        for i in sim_scores:
            if i[1] != np.float64(0.0):
                if idx != i[0]:
                    l.append(lugars.__getitem__(i[0]))
        return l

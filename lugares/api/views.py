import decimal
from datetime import date, timedelta

import numpy as np
from django.db.models import Q
from firebase_admin import auth
from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from BackendTG.permisos import AuthFirebaseUser, IsAdmin, IsOwner
from lugares.models import Lugar
from lugares.models import RecomendacionLugares
from preferencias.models import Preferencia
from suscripciones.models import Suscripcion
from usuarios.models import Usuario
from visitas.models import Visita
from .serializers import LugarSerializer
from .serializers import RecomendacionLugarSerializer


##############################################################################################
class LugaresView(generics.RetrieveUpdateDestroyAPIView):
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
            calificaciones.append(x.calificacion)
            cantidad.append(x.comentario.count())

        np_calificaciones = np.array(calificaciones)
        np_cantidad = np.array(cantidad)

        c = np.mean(np_calificaciones)
        print(c)
        m = np.quantile(np_cantidad, .9)

        for lugar in populares:
            lugar.calificacion = self.weighted_rating(lugar.calificacion, lugar.comentario.count(), m, c)
            lista.append(lugar)

        lista.sort(key=lambda x: x.calificacion, reverse=True)
        for lugar in lista:
            print(lugar.calificacion)
        return lista


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

        # from sklearn.feature_extraction.text import TfidfVectorizer
        # from sklearn.metrics.pairwise import linear_kernel
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

        # Function to convert all strings to lower case and strip names of spaces
        def clean_data(x):
            if isinstance(x, str):
                return str.lower(x.replace(" ", ""))
            else:
                return ''

        lugares = Lugar.objects.all()

        query = self.request.GET.get('usuario')
        preferencia = Preferencia.objects.all().filter(usuario__uid__exact=query)
        user = Usuario.objects.get(uid__exact=query)
        prefer = None
        # descripciones = []
        tags = list(preferencia.values('tags'))
        tagsRS = []
        lugars = []
        for lugar in lugares:
            lugars.append(lugar)

        for p in preferencia:
            prefer = p
        stop_words = ['una', 'el', 'un', 'la', 'es', 'esta', 'de', 'los', 'las', 'unas', 'unos', 'al', 'del', 'lo',
                      'y',
                      'a', 'somos', 'cuenta', 'con', 'porque', 'ya', 'que', 'mas', 'en', 'para', 'su', 'se', 'ha']

        palabras = ''
        for tag in prefer.tags:
            palabras += clean_data(str(tag)) + ' '
            # print(palabras)
        tagsRS.append(palabras)
        lugars.sort(key=lambda x: x.id)
        for lugar in lugars:
            palabras = ''
            # descripciones.append(lugar.descripcion)
            for tag in lugar.tag.all():
                palabras += clean_data(tag.nombre) + ' '
                # print(palabras)
            tagsRS.append(palabras)

        # tfidf = TfidfVectorizer(stop_words=stop_words)
        # tfidf_matrix = tfidf.fit_transform(descripciones)

        # cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        count = CountVectorizer(stop_words=stop_words)
        count_matrix = count.fit_transform(tagsRS)
        cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

        # print(cosine_sim2)

        l = []
        idx = 0
        sim_scores = list(enumerate(cosine_sim2[idx]))
        # print(lugars)
        #print(sim_scores)
        for i in sim_scores:
            if i[1] != np.float64(0.0):
                # print(i[0], i[1])
                if idx != i[0]:
                    #print(lugars.__getitem__(i[0] - 1).id, user.id)
                    try:
                        obj = RecomendacionLugares.objects.get(lugar__id=lugars.__getitem__(i[0] - 1).id, usuario_id=user.id)
                        obj.valor = str(i[1])
                        obj.save()
                    except RecomendacionLugares.DoesNotExist:
                        obj = RecomendacionLugares(lugar=lugars.__getitem__(i[0] - 1), usuario=user, valor=str(i[1]))
                        obj.save()
                    #print(obj)
                    l.append(lugars.__getitem__(i[0] - 1));
        return l


##############################################################################################
class ConsultaRecomendaciones(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = RecomendacionLugarSerializer
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        qs = RecomendacionLugares.objects.all()
        query = self.request.GET.get("lugar")
        query2 = self.request.GET.get("usuario")

        if query is not None:
            qs = qs.filter(Q(lugar__id=query)).distinct() & qs.filter(Q(usuario__uid=query2)).distinct()
        return qs
import decimal
from datetime import date, timedelta

import numpy as np
from django.db.models import Q

from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from lugares.models import Lugar
from visitas.models import Visita
from suscripciones.models import Suscripcion
from .serializers import LugarSerializer

import firebase_admin
from firebase_admin import auth, credentials

cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)

##############################################################################################
class LugaresView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return Lugar.objects.all()
        except:
            return None

    def put(self, request, *args, **kwargs):
        lugar = self.get_object()
        productos = request.data.get('producto')
        for producto in productos:
            print(producto.get('id'))
            if producto.get('id') == 0:
                self.push_notify(nombre_lugar=lugar.nombre, nombre_producto=producto.get('nombre'), id_lugar=lugar.id)
        for producto in lugar.producto.all():
            print(producto.id)
            if producto.id == 0:
                self.push_notify(nombre_lugar=lugar.nombre, nombre_producto=producto.nombre, id_lugar=lugar.id)

        return self.update(request, *args, **kwargs)

    def push_notify(self, nombre_lugar, nombre_producto, id_lugar):
        from pusher_push_notifications import PushNotifications

        pn_client = PushNotifications(
            instance_id='150ee5d4-aa83-42f8-9c65-fe6ab983f0ca',
            secret_key='FA39827AAB5E866F8084A0FD034F5CB59D987D566D35ED66BBEEA1564D561E93',
        )
        message = nombre_lugar + ' ha agregado ' + nombre_producto + ' a sus productos'
        interest = str(id_lugar)
        response = pn_client.publish(
            interests=[interest],
            publish_body={'apns': {'aps': {'alert': 'Hello!'}},
                          'fcm': {'notification': {'title': 'Nuevo Evento', 'body': message}}}
        )

        print(response['publishId'])


##############################################################################################
class LugaresListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)

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

        except:
            return None

    def post(self, request, *args, **kwargs):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)
            return self.create(request, *args, **kwargs)
        except:
            return None

##############################################################################################
class LugaresPopulares(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer

    def weighted_rating(self, calificacion, votos, m, C):
        v = votos
        R = calificacion
        # Calculo de la formula dada por la IMDB

        return (decimal.Decimal(v / (v + m)) * R) + (decimal.Decimal(m / (m + v)) * C)

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)

            global np_calificaciones, np_cantidad
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

        except:
            return None

##############################################################################################
class LugaresUsuarioCount(APIView):
    renderer_classes = (JSONRenderer,)

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

    def get(self, request, format=None):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)

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

        except:
            return None

##############################################################################################
class LugaresVisitados(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)

            qs = Lugar.objects.all()
            query = self.request.GET.get('usuario')
            if query is not None:
                qs = qs.filter((Q(visita__usuario__uid=query)))
            return qs

        except:
            return None

##############################################################################################
class LugaresNuevos(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)

            query = self.request.GET.get('dias')
            lugares = []
            for lugar in Lugar.objects.all():
                hoy = date.today()
                diferencia = hoy - lugar.fecha_creacion
                if diferencia <= timedelta(days=int(query)):
                    lugares.append(lugar)
            return lugares

        except:
            return None

##############################################################################################
class LugaresRecomendados(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = LugarSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_AUTHORIZATION']
            print(token)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print(uid)

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

        except:
            return None


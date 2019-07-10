from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.renderers import JSONRenderer

from BackendTG.permisos import AuthFirebaseUser
from opiniones.models import Opinion
from .serializers import OpinionSerializer

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


class OpinionView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = OpinionSerializer
    renderer_classes = (JSONRenderer,)
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Opinion.objects.all()


class OpinionListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = OpinionSerializer
    renderer_classes = (JSONRenderer,)

    permission_classes = (AuthFirebaseUser,)

    def report(self, pred, data):
        print(pred)
        print(data)

        np.sum(data)
        np.sum(pred)

        print('Accuracy Score: ', accuracy_score(data, pred))
        print(confusion_matrix(data, pred))

        print(classification_report(data, pred))

    def get_queryset(self):
        qs = Opinion.objects.all()
        query = self.request.GET.get("usuario")
        if query is not None:
            qs = qs.filter(Q(usuario__uid__exact=query))
        else:
            query = self.request.GET.get("lugar")
            query2 = self.request.GET.get("uid")
            if query is not None:
                qs = qs.filter(Q(lugar__id__exact=query)).distinct() & qs.filter(
                    Q(usuario__uid__exact=query2)).distinct()
        pred = []
        data = []

        for opinion in qs:
            if (opinion.like):
                data.append(np.int(1))
            else :
                data.append(np.int(0))
            if(opinion.valor == " "):
                opinion.__setattr__("valor", 1)
            if (float(opinion.valor) < 0.5):
                pred.append(np.int(0))
            else:
                pred.append(np.int(1))
        self.report(pred, data)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

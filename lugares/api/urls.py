from django.urls import path
from .views import *


urlpatterns = [
    path('', LugaresListView.as_view(), name='lugar-create'),
    path('<int:id>/', LugaresView.as_view(), name='lugar-rud'),
    path('count/', LugaresUsuarioCount.as_view(), name='lugar-update'),
    path('popular/', LugaresPopulares.as_view(), name='lugar-popular'),
    path('count/data/' , LugaresVisitasCount.as_view(), name='lugar-count'),
    path('visitas/', LugaresVisitados.as_view(), name='lugares-visitados'),
    path('suscrito/', LugaresSuscrito.as_view(), name='lugares-suscrito'),
    path('nuevos/', LugaresNuevos.as_view(), name='lugares-visitados'),
    path('recomendados/', LugaresRecomendados.as_view(), name='lugares-recomendados'),


]

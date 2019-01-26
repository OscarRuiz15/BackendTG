from django.urls import include, path
from .views import EventoListView, EventoView, EventoSuscrito

urlpatterns = [
    path('', EventoListView.as_view(), name='evento-create'),
    path('<int:id>/', EventoView.as_view(), name='evento-rud'),
    path('consulta/', EventoSuscrito.as_view(), name='evento-suscrito')
]

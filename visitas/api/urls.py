from django.urls import path

from .views import VisitasView, VisitasListView, VisitasUsuarioCount

urlpatterns = [
    path('', VisitasListView.as_view(), name='visitas-create'),
    path('count/', VisitasUsuarioCount.as_view(), name='visitas-count'),
    path('<int:id>/', VisitasView.as_view(), name='visitas-rud'),
]

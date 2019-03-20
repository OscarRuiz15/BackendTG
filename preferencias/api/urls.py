from django.urls import path

from .views import PreferenciasView, PreferenciasListView

urlpatterns = [
    path('', PreferenciasListView.as_view(), name='preferencias-create'),
    path('<int:id>/', PreferenciasView.as_view(), name='preferencias-rud'),
]

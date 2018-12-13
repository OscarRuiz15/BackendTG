from django.urls import path
from .views import *

urlpatterns = [
    path('<str:codigo>/', MunicipioViewId.as_view(), name='municipio-rud'),
    path('', MunicipioView.as_view(), name='municipio-rud'),
]
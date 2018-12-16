from django.urls import path
from .views import *


urlpatterns = [
    path('<int:codigo>/', DepartamentoViewId.as_view(), name='deptoId'),
    path('', DepartamentoView.as_view(), name='departamentos'),

]

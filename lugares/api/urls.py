from django.urls import path
from .views import *


urlpatterns = [
    path('', LugaresListView.as_view(), name='lugar-create'),
    path('<int:id>/', LugaresView.as_view(), name='lugar-rud'),
    path('count/', LugaresUsuarioCount.as_view(), name='lugar-update'),

]

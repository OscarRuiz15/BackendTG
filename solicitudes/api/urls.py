
from django.urls import include, path
from .views import SolicitudesView, SolicitudesListView


urlpatterns = [
    path('', SolicitudesListView.as_view(), name='request-create'),
    path('<int:id>/', SolicitudesView.as_view(), name='request-rud'),
]

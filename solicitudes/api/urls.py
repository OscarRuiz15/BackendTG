
from django.urls import include, path
from .views import SolicitudesView, SolictidudesListView


urlpatterns = [
    path('', SolictidudesListView.as_view(), name='request-create'),
    path('<int:id>/', SolicitudesView.as_view(), name='request-rud'),
]


from django.urls import include, path
from .views import SuscripcionView, SuscripcionListView, SuscripcionUsuarioCount


urlpatterns = [
    path('', SuscripcionListView.as_view(), name='request-create'),
    path('<int:id>/', SuscripcionView.as_view(), name='request-rud'),
    path('count/', SuscripcionUsuarioCount.as_view(), name='count-suscripcion')
]

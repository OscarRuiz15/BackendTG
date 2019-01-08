from django.urls import path

from .views import VisitasView, VisitasListView, VisitasUsuarioCount

urlpatterns = [
    path('', VisitasListView.as_view(), name='users-create'),
    path('count/', VisitasUsuarioCount.as_view(), name='users-create'),
    path('<int:id>/', VisitasView.as_view(), name='users-rud'),
]

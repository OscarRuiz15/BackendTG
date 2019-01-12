from django.urls import include, path
from .views import UsuariosView, UsuariosListView, UsuariosCreateView, UsuariosSuscritosView

urlpatterns = [
    path('', UsuariosCreateView.as_view(), name='users-create'),
    path('list/', UsuariosListView.as_view(), name='users-list'),
    path('<str:uid>/', UsuariosView.as_view(), name='users-rud'),
    path('list/suscrito/', UsuariosSuscritosView.as_view(), name='users-subscribed'),
]

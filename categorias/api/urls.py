from django.urls import include, path
from .views import CategoriasView, CategoriasListView


urlpatterns = [
    path('<int:id>/', CategoriasView.as_view(), name='categories-rud'),
    path('', CategoriasListView.as_view(), name='categories-create'),


]
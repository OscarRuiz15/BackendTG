
from django.urls import path
from .views import ComentarioListView, ComentarioView

urlpatterns = [
    path('', ComentarioListView.as_view(), name='comments-create'),
    path('<int:id>/', ComentarioView.as_view(), name='comments-rud'),
]

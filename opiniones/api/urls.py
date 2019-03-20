from django.urls import path

from .views import OpinionView, OpinionListView

urlpatterns = [
    path('', OpinionListView.as_view(), name='opínion-create'),
    path('<int:id>/', OpinionView.as_view(), name='opínion-rud'),
]

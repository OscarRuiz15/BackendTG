from django.urls import path

from .views import TagsView, TagsListView

urlpatterns = [
    path('', TagsListView.as_view(), name='tags-create'),
    path('<int:id>/', TagsView.as_view(), name='tags-rud'),
]

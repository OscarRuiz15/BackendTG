from django.urls import path
from .views import *


urlpatterns = [
    path('', RatingsListView.as_view(), name='rating-create'),
    path('<int:id>/', RatingsView.as_view(), name='rating-rud'),

]

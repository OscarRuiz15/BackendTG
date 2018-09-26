from django.urls import path
from .views import *


urlpatterns = [
    path('<int:id>/', ProductoViewId.as_view(), name='productsId'),
    path('', ProductoView.as_view(), name='products'),

]

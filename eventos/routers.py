from eventos import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Evento',views.EventoViewSite)
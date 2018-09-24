from solicitudes import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Solicitud',views.SolicitudViewSite)
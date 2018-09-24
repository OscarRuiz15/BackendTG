from visitas import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Visita',views.VisitaViewSite)
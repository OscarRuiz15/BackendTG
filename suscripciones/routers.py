from suscripciones import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Suscripcion',views.SuscripcionViewSite)
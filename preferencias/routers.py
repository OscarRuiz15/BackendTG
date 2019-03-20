from preferencias import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Preferencia',views.PreferenciaViewSite)
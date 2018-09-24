from lugares import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Lugar',views.LugarViewSite)
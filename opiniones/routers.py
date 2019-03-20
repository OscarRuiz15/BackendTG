from opiniones import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Opinion',views.OpinionViewSite)
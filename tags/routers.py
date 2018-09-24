from tags import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Tag',views.TagViewSite)
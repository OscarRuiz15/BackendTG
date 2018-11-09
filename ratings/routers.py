from ratings import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Rating',views.RatingViewSite)
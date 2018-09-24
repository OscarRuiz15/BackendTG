from productos import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Producto',views.ProductoViewSite)
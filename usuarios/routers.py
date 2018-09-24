from usuarios import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Usuario',views.UsuarioViewSite)
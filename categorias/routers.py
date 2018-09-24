from categorias import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Categoria',views.CategoriaViewSite)
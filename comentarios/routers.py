from comentarios import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Comentario',views.ComentarioViewSite)
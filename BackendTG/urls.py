"""BackendTG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# from categorias.routers import router as routerCategorias
# from comentarios.routers import router as routerComentarios
# from eventos.routers import router as routerEventos
# from lugares.routers import router as routerLugares
# from productos.routers import router as routerProductos
# from solicitudes.routers import router as routerSolicitudes
# from suscripciones.routers import router as routerSuscripciones
# from tags.routers import router as routerTags
# from usuarios.routers import router as routerUsuarios
# from visitas.routers import router as routerVisitas

# from ratings.routers import router as routerRatings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-auth/', include('rest_framework.urls')),
    # path('categorias/', include(routerCategorias.urls)),
    # path('comentarios/', include(routerComentarios.urls)),
    # path('eventos/', include(routerEventos.urls)),
    # path('lugares/', include(routerLugares.urls)),
    # path('productos/', include(routerProductos.urls)),
    # path('solicitudes/', include(routerSolicitudes.urls)),
    # path('suscripciones/', include(routerSuscripciones.urls)),
    # path('tags/', include(routerTags.urls)),
    # path('usuarios/', include(routerUsuarios.urls)),
    # path('visitas/', include(routerVisitas.urls)),
    # path('ratings/', include(routerRatings.urls)),
    path('usuarios/api/', include(('usuarios.api.urls', 'user'), namespace='api-users')),
    path('categorias/api/', include(('categorias.api.urls', 'category'), namespace='api-category')),
    path('productos/api/', include(('productos.api.urls', 'product'), namespace='api-products')),
    path('tags/api/', include(('tags.api.urls', 'tag'), namespace='api-tags')),
    path('comentarios/api/', include(('comentarios.api.urls', 'comment'), namespace='api-comments')),
    path('visitas/api/', include(('visitas.api.urls', 'request'), namespace='api-visitas')),
    path('solicitudes/api/', include(('solicitudes.api.urls', 'request'), namespace='api-request')),
    path('suscripciones/api/', include(('suscripciones.api.urls', 'request'), namespace='api-suscripciones')),
    path('eventos/api/', include(('eventos.api.urls', 'request'), namespace='api-eventos')),
    path('lugares/api/', include(('lugares.api.urls', 'lugar'), namespace='api-lugar')),
    path('preferencias/api/', include(('preferencias.api.urls', 'lugar'), namespace='api-preferencia')),
    path('opiniones/api/', include(('opiniones.api.urls', 'lugar'), namespace='api-opiniones')),
    # path('ratings/api/', include(('ratings.api.urls', 'rating'), namespace='api-rating')),
    # path('departamentos/api/', include(('departamentos.api.urls', 'departamentos'), namespace='api-departamento')),
    # path('municipios/api/', include(('municipios.api.urls', 'municipios'), namespace='api-municipios')),

    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
]

from django.contrib import admin
# Register your models here.
from lugares.models import Lugar
from lugares.models import RecomendacionLugares

admin.site.register(Lugar)
admin.site.register(RecomendacionLugares)
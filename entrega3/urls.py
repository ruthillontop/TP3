from django.urls import path, include
from empleados.views import empleados, alta_empleados, lista_empleados, buscar_empleados
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('empleados/', include('empleados.urls')),
    path('destinos/', include('destinos.urls')),
    path('pasajeros/', include('pasajeros.urls')),
]

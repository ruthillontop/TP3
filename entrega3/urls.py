from django.urls import path, include
from empleados.views import empleados, alta_empleados, lista_empleados, buscar_empleados, home, EmpleadosListView, register
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empleados/', include('empleados.urls')),
    path('destinos/', include('destinos.urls')),
    path('pasajeros/', include('pasajeros.urls')),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('cbv/employee-list', EmpleadosListView.as_view(), name='cbv-employee-list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    

    
]

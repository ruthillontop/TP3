from django.urls import path
from empleados.views import empleados, alta_empleados, lista_empleados, buscar_empleados


app_name = "empleados"

urlpatterns = [
    path('', empleados, name='index_empleados'),
    path('alta/', alta_empleados, name='alta-empleados'),
    path('lista/', lista_empleados, name='lista-empleados'),
    path('buscar/', buscar_empleados, name='buscar-empleados'),
    

]
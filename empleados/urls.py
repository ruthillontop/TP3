from django.urls import path
from empleados.views import (
    empleados, alta_empleados, lista_empleados, buscar_empleados, home,
    EmpleadosCreateView, EmpleadosListView, EmpleadosDetailView,
    EmpleadosUpdateView, EmpleadosDeleteView
)

app_name = "empleados"

urlpatterns = [
    path('', empleados, name='index_empleados'),
    path('alta/', alta_empleados, name='alta-empleados'),
    path('lista/', lista_empleados, name='lista-empleados'),
    path('buscar/', buscar_empleados, name='buscar-empleados'),
    
    path("home", home, name="home"),
    path("cbv/empleados-create", EmpleadosCreateView.as_view(), name="cbv-alta-empleados"),
    path("cbv/employee-list", EmpleadosListView.as_view(), name="cbv-employee-list"),
    path("cbv/empleados/<int:pk>", EmpleadosDetailView.as_view(), name="cbv-empleados-detail"),
    path("cbv/empleados/<int:pk>/editar", EmpleadosUpdateView.as_view(), name="cbv-empleados-editar"),
    path("cbv/empleados/<int:pk>/eliminar", EmpleadosDeleteView.as_view(), name="cbv-empleados-eliminar"),

]
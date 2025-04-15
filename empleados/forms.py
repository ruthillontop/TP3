from django.forms import ModelForm

from .models import Empleados


class EmpleadosForm(ModelForm):
    
    class Meta:
        model = Empleados

        fields = ["nombreempleado", "email", "antiguedad", "tipo"]


class EmpleadosBusquedaForm(ModelForm):
    
    class Meta:
        model = Empleados

        fields = ["nombreempleado"]
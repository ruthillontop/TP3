from django.forms import ModelForm

from .models import Destinos


class DestinosForm(ModelForm):
    
    class Meta:
        model = Destinos

        fields = ["ciudad", "pais"]


class DestinosBusquedaForm(ModelForm):
    
    class Meta:
        model = Destinos

        fields = ["pais"]
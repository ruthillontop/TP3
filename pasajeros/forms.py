from django.forms import ModelForm

from .models import Pasajeros


class PasajerosForm(ModelForm):
    
    class Meta:
        model = Pasajeros

        fields = ["nombrepax", "email", "viajero_frecuente", "status"]


class PasajerosBusquedaForm(ModelForm):
    
    class Meta:
        model = Pasajeros
    
        fields = ["nombrepax"]


        #nombrepax = forms.CharField(label="Nombre del pasajero", max_length=50)
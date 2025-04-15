
from django.urls import path
from pasajeros.views import pasajeros, alta_pasajeros, lista_pasajeros, buscar_pasajeros

app_name = "pasajeros"

urlpatterns = [
    path('', pasajeros, name='index_pasajeros'),
    path('alta/', alta_pasajeros, name='alta-pasajeros'),
    path('lista/', lista_pasajeros, name='lista-pasajeros'),
    path('buscar/', buscar_pasajeros, name='buscar-pasajeros'),
]
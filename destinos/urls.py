
from django.urls import path
from destinos.views import destinos, alta_destinos, lista_destinos, buscar_destinos

app_name = "destinos"

urlpatterns = [
    path('', destinos, name='index_destinos'),
    path('alta/', alta_destinos, name='alta-destinos'),
    path('lista/', lista_destinos, name='lista-destinos'),
    path('buscar/', buscar_destinos, name='buscar-destinos'),
]
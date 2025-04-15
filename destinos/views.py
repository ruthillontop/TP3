from django.shortcuts import render
from django.http import HttpResponse
from destinos.models import Destinos
from destinos.forms import DestinosForm, DestinosBusquedaForm
from django.shortcuts import redirect


def destinos(request):
    return render(request, 'destinos/destinos.html')

def alta_destinos(request):

    if request.method == "GET":
        print("El metodo fue un get!")

        contexto = {"formulario": DestinosForm()}
        return render(request, 'destinos/DestinosForm.html', context=contexto)
    else:
       
        print("El metodo fue POST")
        print(request.POST)

        formulario = DestinosForm(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            modelo_de_base_de_datos = Destinos(
                ciudad=datos["ciudad"],
                pais=datos["pais"],
            
            )
            modelo_de_base_de_datos.save()

            return redirect("destinos:lista-destinos")


def lista_destinos(request):

    modelos = destinos.objects.all()
    contexto = {
        "lugares": modelos
    }
    return render(request, 'destinos/lista-destinos.html', context=contexto)


def buscar_destinos(request):
    if request.method == "GET":
       contexto = {"formulario": DestinosBusquedaForm()}
       return render(request, 'empleados/buscar-empleados.html', context=contexto)
    else:
        # procesamos el formulario y devolvemos un resultado
        formulario = DestinosBusquedaForm(request.POST)

        if formulario.is_valid():
            ciudad = formulario.cleaned_data["ciudad"]
            pais = Destinos.objects.filter(nombre__icontains=ciudad)

            contexto = {
                "destinos": destinos,
            }
            return render(request, 'destinos/detail_destinos.html', context=contexto)
        
        # si no es válido, volvemos a mostrar el form con errores
        contexto = {"formulario": DestinosBusquedaForm()}
        return render(request, 'destinos/buscar-destinos.html', context=contexto)
from django.shortcuts import render
from django.http import HttpResponse
from pasajeros.models import Pasajeros

from pasajeros.forms import PasajerosForm, PasajerosBusquedaForm
from django.shortcuts import redirect

def pasajeros(request):
    return render(request, 'pasajeros/pasajeros.html')


def alta_pasajeros(request):

    if request.method == "GET":
        print("El metodo fue un get!")

        contexto = {"formulario": PasajerosForm()}
        return render(request, 'pasajeros/PasajerosForm.html', context=contexto)
    else:
       
        print("El metodo fue POST")
        print(request.POST)

        formulario = PasajerosForm(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            modelo_de_base_de_datos = Pasajeros(
                nombre=datos["nombrepax"],
                email=datos["email"],
                viajero_frecuente= datos["viajero_frecuente"],
                status=datos["status"],
            )
            modelo_de_base_de_datos.save()

            return redirect("pasajeros:lista-pasajeros")


def lista_pasajeros(request):

    modelos = Pasajeros.objects.all()
    contexto = {
        "integrantes": modelos
    }
    return render(request, 'pasajeros/lista-pasajeros.html', context=contexto)


def buscar_pasajeros(request):
    if request.method == "GET":
       contexto = {"formulario": PasajerosBusquedaForm()}
       return render(request, 'pasajeros/buscar-pasajeros.html', context=contexto)
    else:
        # procesamos el formulario y devolvemos un resultado
        formulario = PasajerosBusquedaForm(request.POST)

        if formulario.is_valid():
            nombre = formulario.cleaned_data["nombrepax"]
            viajeros = Pasajeros.objects.filter(nombre__icontains=nombre)

            contexto = {
                "pasajeros": pasajeros,
            }
            return render(request, 'pasajeros/detail_pasajeros.html', context=contexto)
        
        # si no es válido, volvemos a mostrar el form con errores
        contexto = {"formulario": PasajerosBusquedaForm()}
        return render(request, 'pasajeros/buscar-pasajeros.html', context=contexto)
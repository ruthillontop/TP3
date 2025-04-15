from django.shortcuts import render
from django.http import HttpResponse
from empleados.models import Empleados

from empleados.forms import EmpleadosForm, EmpleadosBusquedaForm
from django.shortcuts import redirect

def empleados(request):
    return render(request, 'empleados/empleados.html')

def alta_empleados(request):

    if request.method == "GET":
        print("El metodo fue un get!")

        contexto = {"formulario": EmpleadosForm()}
        return render(request, 'empleados/EmpleadosForm.html', context=contexto)
    else:
       
        print("El metodo fue POST")
        print(request.POST)

        formulario = EmpleadosForm(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            modelo_de_base_de_datos = Empleados(
                nombreempleado=datos["nombreempleado"],
                email=datos["email"],
                antiguedad=datos["antiguedad"]
            )
            modelo_de_base_de_datos.save()

            return redirect("empleados:lista-empleados")


def lista_empleados(request):

    modelos = Empleados.objects.all()
    contexto = {
        "trabajadores": modelos
    }
    return render(request, 'empleados/lista-empleados.html', context=contexto)


def buscar_empleados(request):
    if request.method == "GET":
       contexto = {"formulario": EmpleadosBusquedaForm()}
       return render(request, 'empleados/buscar-empleados.html', context=contexto)
    else:
        # procesamos el formulario y devolvemos un resultado
        formulario = EmpleadosBusquedaForm(request.POST)

        if formulario.is_valid():
            nombre = formulario.cleaned_data["nombreempleado"]
            empleados_filtrados = Empleados.objects.filter(nombreempleado__icontains=nombre)

            contexto = {
                "empleados": empleados_filtrados,
            }
                        
            return render(request, 'empleados/detail_empleados.html', context=contexto)
        
        # si no es válido, volvemos a mostrar el form con errores
        contexto = {"formulario": EmpleadosBusquedaForm()}
        return render(request, 'empleados/buscar_empleados.html', context=contexto)
    

    
from django.shortcuts import render, redirect
from django.http import HttpResponse
from empleados.models import Empleados

from empleados.forms import EmpleadosForm, EmpleadosBusquedaForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def empleados(request):
    return render(request, 'empleados/empleados.html')

def home (request):
    return render (request,'empleados/home.html')

@login_required
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
        "empleados": modelos
    }
    return render(request, 'empleados/lista_empleados.html', context=contexto)


def buscar_empleados(request):
    if request.method == "GET":
       contexto = {"formulario": EmpleadosBusquedaForm()}
       return render(request, 'empleados/buscar_empleados.html', context=contexto)
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
    

    
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class EmpleadosListView(ListView):
    model = Empleados
    template_name = 'empleados/cbv/employee-list.html'
    context_object_name = 'empleados'


class EmpleadosCreateView(LoginRequiredMixin, CreateView):
    model = Empleados
    fields = ['nombreempleado', 'email', 'antiguedad', 'tipo']
    template_name = "empleados/cbv/empleados-create.html"
    success_url = reverse_lazy('empleados:cbv-alta-empleados')
    login_url = 'login'


class EmpleadosDetailView(DetailView):
    model = Empleados
    template_name = "empleados/cbv/empleados-detail.html"


class EmpleadosUpdateView(UpdateView):
    model = Empleados
    fields = ["nombreempleado", "email", "antiguedad", "tipo"]
    template_name = "empleados/cbv/empleados-edit.html" 
    success_url = reverse_lazy("empleados:cbv-employee-list")





class EmpleadosDeleteView(DeleteView):
    model = Empleados
    template_name = "empleados/cbv/empleados-eliminar.html"
    success_url = reverse_lazy("empleados:cbv-employee-list")

class HomeView(TemplateView):
    template_name = "empleados/home.html"



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'empleados/register.html', {'form': form})

def acerca_de_mi(request):
    return render(request, 'empleados/acerca.html')
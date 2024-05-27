from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vuelo, Avion, Empleado
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    return HttpResponse("¡Hola 🌍!, esta es la página de Nyandü (en construcción)")


@login_required
def principal(request):
    return render(
    request,
    'nyandu/principal.html',
     context={},
)


class VueloListView(generic.ListView):
    model = Vuelo


class VueloDetailView(generic.DetailView):
    model = Vuelo

class AvionListView(generic.ListView):
    model = Avion


class AvionDetailView(generic.DetailView):
    model = Avion


class AvionCreate(CreateView):
    model = Avion
    fields = '__all__'

class AvionUpdate(UpdateView):
    model = Avion
    fields = '__all__'

class AvionDelete(DeleteView):
    model = Avion
    success_url = reverse_lazy('aviones')


class EmpleadoListView(generic.ListView):
    model = Empleado


class EmpleadoDetailView(generic.DetailView):
    model = Empleado


class EmpleadoCreate(CreateView):
    model = Empleado
    fields = '__all__'

class EmpleadoUpdate(UpdateView):
    model = Empleado
    fields = ['nombre_completo','telefono']

class EmpleadoDelete(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Eleccion


class RegistrarEleccion(CreateView):
    template_name = 'elecciones/eleccion.html'
    model = Eleccion
    success_url = reverse_lazy("listar_eleccion")


class ListarEleccion(ListView):
    model = Eleccion
    template_name = 'elecciones/listar.html'
    context_object_name = "listar_eleccion"
    paginate_by = 10


class EditarEleccion(UpdateView):
    model = Eleccion
    template_name = 'elecciones/modificar.html'
    context_object_name = "editar_eleccion"
    success_url = reverse_lazy("listar_eleccion")


class BorrarEleccion(DeleteView):
    model = Eleccion
    template_name = 'elecciones/borrar.html'
    context_object_name = "borrar_eleccion"
    success_url = reverse_lazy("listar_eleccion")

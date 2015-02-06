from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Tipo_eleccion


class RegistrarTipo_eleccion(CreateView):
    template_name = 'tipos_eleccion/tipos.html'
    model = Tipo_eleccion
    success_url = reverse_lazy("listar_tipos")


class ListarTipo_eleccion(ListView):
    model = Tipo_eleccion
    template_name = 'tipos_eleccion/listar.html'
    context_object_name = "listar_tipos"
    paginate_by = 10


class EditarTipo_eleccion(UpdateView):
    model = Tipo_eleccion
    template_name = 'tipos_eleccion/modificar.html'
    context_object_name = "editar_tipos"
    success_url = reverse_lazy("listar_tipos")


class BorrarTipo_eleccion(DeleteView):
    model = Tipo_eleccion
    template_name = 'tipos_eleccion/borrar.html'
    context_object_name = "borrar_tipos"
    success_url = reverse_lazy("listar_tipos")

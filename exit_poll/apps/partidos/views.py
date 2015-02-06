from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Partidos


class RegistrarPartidos(CreateView):
    template_name = 'partido/partido.html'
    model = Partidos
    success_url = reverse_lazy("listar_partido")


class ListarPartidos(ListView):
    model = Partidos
    template_name = 'partido/listar.html'
    context_object_name = "listar_partido"
    paginate_by = 10


class EditarPartidos(UpdateView):
    model = Partidos
    template_name = 'partido/modificar.html'
    context_object_name = "editar_partido"
    success_url = reverse_lazy("listar_partido")


class BorrarPartidos(DeleteView):
    model = Partidos
    template_name = 'partido/borrar.html'
    context_object_name = "borrar_partido"
    success_url = reverse_lazy("listar_partido")

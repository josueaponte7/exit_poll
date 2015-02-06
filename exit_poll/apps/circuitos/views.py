from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Circuito


class RegistrarCircuito(CreateView):
    template_name = 'circuito/circuito.html'
    model = Circuito
    success_url = reverse_lazy("listar_circuito")


class ListarCircuito(ListView):
    model = Circuito
    template_name = 'circuito/listar.html'
    context_object_name = "listar_circuito"
    paginate_by = 10


class EditarCircuito(UpdateView):
    model = Circuito
    template_name = 'circuito/modificar.html'
    context_object_name = "editar_circuito"
    success_url = reverse_lazy("listar_circuito")


class BorrarCircuito(DeleteView):
    model = Circuito
    template_name = 'circuito/borrar.html'
    context_object_name = "borrar_circuito"
    success_url = reverse_lazy("listar_circuito")

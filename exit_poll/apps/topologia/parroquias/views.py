from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Parroquia


class RegistrarParroquia(CreateView):
    template_name = 'topologia/parroquias/parroquias.html'
    model = Parroquia
    success_url = reverse_lazy("listar_parroquia")


class ListarParroquia(ListView):
    model = Parroquia
    template_name = 'topologia/parroquias/listar.html'
    context_object_name = "listar_parroquia"
    paginate_by = 10


class EditarParroquia(UpdateView):
    model = Parroquia
    template_name = 'topologia/parroquias/modificar.html'
    context_object_name = "editar_parroquia"
    success_url = reverse_lazy("listar_parroquia")


class BorrarParroquia(DeleteView):
    model = Parroquia
    template_name = 'topologia/parroquias/borrar.html'
    context_object_name = "borrar_parroquia"
    success_url = reverse_lazy("listar_parroquia")

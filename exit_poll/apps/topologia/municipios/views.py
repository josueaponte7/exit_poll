from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Municipio


class RegistrarMunicipio(CreateView):
    template_name = 'topologia/municipios/municipios.html'
    model = Municipio
    success_url = reverse_lazy("listar_municipio")


class ListarMunicipio(ListView):
    model = Municipio
    template_name = 'topologia/municipios/listar.html'
    context_object_name = "listar_municipio"
    paginate_by = 10


class EditarMunicipio(UpdateView):
    model = Municipio
    template_name = 'topologia/municipios/modificar.html'
    context_object_name = "editar_municipio"
    success_url = reverse_lazy("listar_municipio")


class BorrarMunicipio(DeleteView):
    model = Municipio
    template_name = 'topologia/municipios/borrar.html'
    context_object_name = "borrar_municipio"
    success_url = reverse_lazy("listar_municipio")

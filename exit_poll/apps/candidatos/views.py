from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Candidatos


class RegistrarCandidatos(CreateView):
    template_name = 'candidato/candidato.html'
    model = Candidatos
    success_url = reverse_lazy("listar_candidato")


class ListarCandidatos(ListView):
    model = Candidatos
    template_name = 'candidato/listar.html'
    context_object_name = "listar_candidato"
    paginate_by = 10


class EditarCandidatos(UpdateView):
    model = Candidatos
    template_name = 'candidato/modificar.html'
    context_object_name = "editar_candidato"
    success_url = reverse_lazy("listar_candidato")


class BorrarCandidatos(DeleteView):
    model = Candidatos
    template_name = 'candidato/borrar.html'
    context_object_name = "borrar_candidato"
    success_url = reverse_lazy("listar_candidato")
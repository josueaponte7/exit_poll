from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Estado
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .forms import EstadoForm


class RegistrarEstado(FormView):
    template_name = 'topologia/estados/estados.html'
    model = Estado
    success_url = reverse_lazy("listar_estado")
    form_class = EstadoForm

    def form_valid(self, form):
        form.save()
        return super(RegistrarEstado, self).form_valid(form)


class ListarEstado(ListView):
    model = Estado
    template_name = 'topologia/estados/listar.html'
    context_object_name = "listar_estado"
    paginate_by = 5


class EditarEstado(UpdateView):
    model = Estado
    template_name = 'topologia/estados/modificar.html'
    context_object_name = "editar_estado"
    success_url = reverse_lazy("listar_estado")


class BorrarEstado(DeleteView):
    model = Estado
    template_name = 'topologia/estados/borrar.html'
    context_object_name = "borrar_estado"
    success_url = reverse_lazy("listar_estado")

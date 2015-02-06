from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Categoria
from django.views.generic.edit import FormView
from apps.tipos.categoria_eleccion.forms import CategoriaForm


class RegistrarCategoria(FormView):
    template_name = 'categoria_eleccion/categoria.html'
    model = Categoria
    success_url = reverse_lazy("listar_categoria")
    form_class = CategoriaForm

    def form_valid(self, form):
        form.save()
        return super(RegistrarCategoria, self).form_valid(form)


class ListarCategoria(ListView):
    model = Categoria
    template_name = 'categoria_eleccion/listar.html'
    context_object_name = "listar_categoria"
    paginate_by = 10


class EditarCategoria(UpdateView):
    model = Categoria
    template_name = 'categoria_eleccion/modificar.html'
    context_object_name = "editar_categoria"
    success_url = reverse_lazy("listar_categoria")


class BorrarCategoria(DeleteView):
    model = Categoria
    template_name = 'categoria_eleccion/borrar.html'
    context_object_name = "borrar_categoria"
    success_url = reverse_lazy("listar_categoria")

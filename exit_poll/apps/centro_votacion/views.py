from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Centros
from django.views.generic.edit import FormView
from apps.centro_votacion.forms import CentrosForm
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia


class RegistrarCentros(FormView):
    template_name = 'centros/centros.html'
    model = Centros
    fields = ['codigo', 'nombre', 'estado', 'municipio', 'parroquia', 'direccion']
    success_url = reverse_lazy("listar_centros")
    form_class = CentrosForm

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(RegistrarCentros, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['list_e'] = Estado.objects.all()
        context['list_m'] = Municipio.objects.all()
        context['list_p'] = Parroquia.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super(RegistrarCentros, self).form_valid(form)


class ListarCentros(ListView):
    model = Centros
    template_name = 'centros/listar.html'
    context_object_name = "listar_centros"
    paginate_by = 10


class EditarCentros(UpdateView):
    model = Centros
    template_name = 'centros/modificar.html'
    context_object_name = "editar_centros"
    success_url = reverse_lazy("listar_centros")

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(EditarCentros, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['list_e'] = Estado.objects.all()
        context['list_m'] = Municipio.objects.all()
        context['list_p'] = Parroquia.objects.all()
        return context


class BorrarCentros(DeleteView):
    model = Centros
    template_name = 'centros/borrar.html'
    context_object_name = "borrar_centros"
    success_url = reverse_lazy("listar_centros")

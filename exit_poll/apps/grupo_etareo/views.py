from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Grupo_Etareo
from apps.grupo_etareo.forms import Grupo_EtareoForm
from django.views.generic.edit import FormView


class RegistrarGrupo_Etareo(FormView):
    template_name = 'grupo_etareo/grupo_etareo.html'
    model = Grupo_Etareo
    success_url = reverse_lazy("listar_grupo_etareo")
    form_class = Grupo_EtareoForm

    def form_valid(self, form):
        form.save()
        return super(RegistrarGrupo_Etareo, self).form_valid(form)


class ListarGrupo_Etareo(ListView):
    model = Grupo_Etareo
    template_name = 'grupo_etareo/listar.html'
    context_object_name = "listar_grupo_etareo"
    paginate_by = 10


class EditarGrupo_Etareo(UpdateView):
    model = Grupo_Etareo
    template_name = 'grupo_etareo/modificar.html'
    context_object_name = "editar_grupo_etareo"
    success_url = reverse_lazy("listar_grupo_etareo")


class BorrarGrupo_Etareo(DeleteView):
    model = Grupo_Etareo
    template_name = 'grupo_etareo/borrar.html'
    context_object_name = "borrar_grupo_etareo"
    success_url = reverse_lazy("listar_grupo_etareo")

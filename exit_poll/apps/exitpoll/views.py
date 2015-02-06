from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import ExitPoll


class RegistrarExitPoll(CreateView):
    template_name = 'exitpoll/exitpoll.html'
    model = ExitPoll
    success_url = reverse_lazy("listar_exitpoll")


class ListarExitPoll(ListView):
    model = ExitPoll
    template_name = 'exitpoll/listar.html'
    context_object_name = "listar_exitpoll"
    paginate_by = 10


class EditarExitPoll(UpdateView):
    model = ExitPoll
    template_name = 'exitpoll/modificar.html'
    context_object_name = "editar_exitpoll"
    success_url = reverse_lazy("listar_exitpoll")


class BorrarExitPoll(DeleteView):
    model = ExitPoll
    template_name = 'exitpoll/borrar.html'
    context_object_name = "borrar_exitpoll"
    success_url = reverse_lazy("listar_exitpoll")


class Candidatos(ListView):
    model = ExitPoll
    template_name = 'exitpoll/candidatos.html'
    context_object_name = "listar_exitpoll"
    paginate_by = 10

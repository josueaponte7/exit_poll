from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import Votacion

class RegistrarVotacion(CreateView):
    template_name = 'votacion/votar.html'
    model = Votacion
    fields = ['grupo_etareo', 'candidatos']
    success_url = reverse_lazy("votar")
    
    

class ListarVotacion(ListView):
    model = Votacion
    template_name = 'votacion/listar1.html'
    context_object_name = "listar_votacion"
    paginate_by = 10

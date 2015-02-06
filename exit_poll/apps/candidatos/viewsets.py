from .models import Candidatos
from .serializers import CandidatosSerializer
from rest_framework import serializers, viewsets


class CandidatosViewSet(viewsets.ModelViewSet):

    serializer_class = CandidatosSerializer
    queryset = Candidatos.objects.all()


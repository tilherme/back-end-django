from rest_framework.viewsets import ModelViewSet
from avaliacao.models import Avaliacao 
from .serializers import AvaliacaoSerializer  

class AvaliacaoViewsets(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

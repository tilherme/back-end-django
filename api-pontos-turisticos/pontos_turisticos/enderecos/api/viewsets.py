from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecosSerializer
from rest_framework.filters import SearchFilter
class EnderecoViewsets(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecosSerializer
    filter_backends = [SearchFilter]
    search_fields = ['cidade']
    lookup_fields = 'linha2'
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import pontos_turisticos

from .serialeizers import pontos_turisticosSerializers
class PontoTuristicoViewsets(ModelViewSet):

    serializer_class = pontos_turisticosSerializers
    permission_classes = [DjangoModelPermissions]
    authentication_classes = (TokenAuthentication, )
        
    def get_queryset(self):
        
        """
        id = self.request.query_params.get('id',None)
        nome = self.request.query_params.get('nome',None)
        descricao = self.request.query_params.get('descricao',None)
        queryset = pontos_turisticos.objects.all()
        if id:
            queryset = pontos_turisticos.objects.filter(id=id)
        if nome:
            queryset = queryset.filter(nome_iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao_iexact=descricao)
            return queryset"""
def list(self, request, **kwargs):
  return super(pontos_turisticos, self).list(request, **kwargs)

def create(self, request, **kwargs):
   return super(pontos_turisticos, self).create(request, **kwargs)

def destroy(self, request, **kwargs):
   return super(pontos_turisticos, self).destroy(request, **kwargs)


def retrieve(self, request, **kwargs):
    return super(pontos_turisticos, self).retrieve(request, **kwargs)
    
def update(self, request, **kwargs):
    pass
    
def partial_update(self, request, **kwargs):
      return super(pontos_turisticos, self).partial_update(request, **kwargs)

@action(methods=['get'],detail=True) 
def denuciar(self, request, pk=None):
      pass
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import pontos_turisticos

from .serialeizers import pontos_turisticosSerializers
class PontoTuristicoViewsets(ModelViewSet):

    serializer_class = pontos_turisticosSerializers
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return pontos_turisticos.objects.filter(aprovado=True)
  
   
def list(self, request, **kwargs):
   return response({'teste':1234})

def create(self, request, **kwargs):
   return Response({'hello':request.data['nome']})

def destroy(self, request, **kwargs):
    pass


def retrieve(self, request, **kwargs):
    pass
    
def update(self, request, **kwargs):
    pass
    
def partial_update(self, request, **kwargs):
        pass

@action(methods=['get'],detail=True) 
def denuciar(self, request, pk=None):
      pass
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from atracoes.models import Atracao
from rest_framework import filters
from rest_framework import generics
from .serializers import AtracaoSerializer 

class AtracaoViewsets(ModelViewSet):
    queryset= Atracao.objects.all()
    serializer_class = AtracaoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_fields = ('nome', 'descricao', )
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from core.models import pontos_turisticos

from .serialeizers import pontos_turisticosSerializers
class PontoTuristicoViewsets(ModelViewSet):
    queryset= pontos_turisticos.objects.all()
    serializer_class = pontos_turisticosSerializers
    permission_classes = [permissions.IsAuthenticated]

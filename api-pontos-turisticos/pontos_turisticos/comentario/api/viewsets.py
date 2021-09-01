from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from comentario.models import Comentario
from .serializer import ComentarioSerializer 

class ComentarioViewset(ModelViewSet):
    queryset= Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticated]

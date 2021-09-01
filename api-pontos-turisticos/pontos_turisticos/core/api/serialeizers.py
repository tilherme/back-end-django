from rest_framework.serializers import ModelSerializer 
from core.models import pontos_turisticos


class pontos_turisticosSerializers(ModelSerializer):
    class Meta:
        model = pontos_turisticos
        fields = ('id', 'nome', 'descricao', 'aprovado')

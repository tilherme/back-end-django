
from rest_framework.serializers import ModelSerializer 
from core.models import pontos_turisticos
from enderecos.api.serializers import EnderecosSerializer
from atracoes.api.serializers import AtracaoSerializer
class pontos_turisticosSerializers(ModelSerializer):
    enderecos = EnderecosSerializer() 
    atracoes = AtracaoSerializer(many = True)
    class Meta:
        model = pontos_turisticos
        fields = ('id', 'nome', 'descricao', 'aprovado','atracoes','comentarios','avalicoes','enderecos', 'foto','tudo', )
       
    
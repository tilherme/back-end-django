from django.db import models
from atracoes.models import Atracao
from comentario.models import Comentario
from avaliacao.models import Avaliacao
from enderecos.models import Endereco 
class pontos_turisticos(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avalicoes = models.ManyToManyField(Avaliacao)
    enderecos =models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turiscos',null=True, blank=True)
    def __str__(self):
        return self.nome
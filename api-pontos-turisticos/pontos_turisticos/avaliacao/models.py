from django.db import models
from django.contrib.auth.models import User

class Avaliacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentarios = models.TextField(null=True, blank=True)
    nota = models.DecimalField(max_digits=3,decimal_places=2)
    database = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
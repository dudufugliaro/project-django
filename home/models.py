from django.db import models

# Create your models here.
from django.db import models


class Mensagem(models.Model):
    titulo = models.CharField(max_length=120)
    conteudo = models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=80, default="Anônimo")   

    class Meta:
        ordering = ["-criada_em"]

    def __str__(self):
        return self.titulo
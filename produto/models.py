from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=225)
    descricao_curta = models.TextField(max_length=225)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m',blank=True,null=True)
    preco_marting = models.FloatField()
    preco_marting_promocional = models.FloatField(default=0)
    slug = models.SlugField(unique=True)
    tipo = models.CharField(default='V',max_length=1,choices=(('V','Variação'),('S','Simples'),))

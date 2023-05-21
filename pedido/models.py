from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Chave estrangeira para a tabela de usuários do Django
    total = models.FloatField()  # Valor total do pedido (campo float)
    status = models.CharField(
        default="C",  # Valor padrão para o campo de status
        max_length=1,
        choices=(
            ('A', 'Aprovado'),  # Opção Aprovado
            ('C', 'Criado'),  # Opção Criado
            ('R', 'Reprovado'),  # Opção Reprovado
            ('P', 'Pendente'),  # Opção Pendente
            ('E', 'Enviado'),  # Opção Enviado
            ('F', 'Finalizado'),  # Opção Finalizado
        )
    )
    def __str__(self):
        return f'Pedido N.{self.pk}'
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)  # Chave estrangeira para o modelo Pedido
    produto = models.CharField(max_length=255)  # Nome do produto
    produto_id = models.PositiveIntegerField()  # ID do produto
    variacao = models.CharField(max_length=255)  # Nome da variação do produto
    variacao_id = models.PositiveIntegerField()  # Id da variação do produto
    preco = models.FloatField()  # Preço do item
    preco_promocional = models.FloatField(default=0)  # Preço promocional do item (padrão: 0)
    quantidade = models.PositiveIntegerField()  # Quantidade do item
    imagem = models.CharField(max_length=2000)  # URL da imagem do produto

    def __str__(self):
        return f'Item do {self.produto}'

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'
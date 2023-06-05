from IPython.core.display_functions import display
from django.contrib import admin

from produto.models import Produto, Variacao
from . import models
# Register your models here.

class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    list_display  = ['nome','descricao_curta','get_preco_formatado','get_preco_promocional_formatado']
    inlines = [
        VariacaoInline
    ]

admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Variacao)

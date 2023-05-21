from django.contrib import admin

from produto.models import Produto, Variacao
from . import models
# Register your models here.

class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]

admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Variacao)

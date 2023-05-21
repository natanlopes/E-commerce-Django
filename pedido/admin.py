from django.contrib import admin
from . import models

class ItemPedidoInline(admin.TabularInline):
    model = models.ItemPedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]
# Registra o modelo Pedido no painel de administração com o admin personalizado PedidoAdmin
admin.site.register(models.Pedido, PedidoAdmin)
# Registra o modelo ItemPedido no painel de administração
admin.site.register(models.ItemPedido)

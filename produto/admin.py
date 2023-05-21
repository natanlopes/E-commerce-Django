from django.contrib import admin

from produto.models import Produto, Variacao

# Register your models here.

admin.site.register(Produto)
admin.site.register(Variacao)

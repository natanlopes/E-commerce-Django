from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . import models
class ListaProdutos(ListView):
   model = models.Produto
   template_name = 'produto/lista.html'
   context_object_name = 'produtos'
   paginate_by = 10
class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DetalheProduto')
class AdcionarAoCarinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('AdcionarAoCarinho')
class RemoverDoCarinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('RemoverDoCarinho')
class Carinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carinho')
class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')


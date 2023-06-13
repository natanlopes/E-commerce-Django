from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('ListaProdutos')
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


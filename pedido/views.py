from django.shortcuts import render
from  django.views.generic import ListView
from django.http import HttpRequest, HttpResponse
from django.views import View

class Pagar(View):
   def get(self,*args,**kwargs):
      return HttpResponse('Pagar')
class SalvarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('FecharPedido')
class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')
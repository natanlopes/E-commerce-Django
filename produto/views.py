import self as self
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from . import models
from django.contrib import messages
class ListaProdutos(ListView):
   model = models.Produto
   template_name = 'produto/lista.html'
   context_object_name = 'produtos'
   paginate_by = 7
class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = "slug"
class AdcionarAoCarinho(View):

    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
         )
        variacao_id = self.request.GET.get('vid')
        if not variacao_id:
            messages.error(
                self.request,
                'Produto nao existe')
            return redirect(http_referer)
        variacao = get_object_or_404(models.Variacao,id=variacao_id)
        if not self.request.session.get('carinho'):
            self.request.session['carinho'] = {}
            self.request.session.save()
        carrinho = self.request.session['carinho']
        if variacao_id in carrinho:
             # TODO: Variacao existe no carinho
             pass
        else:
             # TODO: Variacao nao existe no carinho
             pass
        return HttpResponse(f'{variacao.produto}{variacao.nome}')
class RemoverDoCarinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('RemoverDoCarinho')
class Carinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carinho')
class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')


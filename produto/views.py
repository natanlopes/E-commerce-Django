import self as self
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from . import models
from pprint import pprint
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
          # TODO : remover linhas abaixo
        # if self.request.session.get('carrinho'):
        #     del self.request.session['carrinho']
        #     self.request.session.save()
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
        variacao_estoque = variacao.estoque
        produto = variacao.produto

        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''

        preco_unitario = variacao.preco
        preco_unitario_promocianal = variacao.preco_promocional
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem

        if imagem:
            imagem = imagem.name
        else:
            imagem = ''

        if variacao.estoque < 1:
             messages.error(
                 self.request,
                 'Estoque insuficiente'
             )
             return redirect(http_referer)


        if not self.request.session.get('carinho'):
            self.request.session['carinho'] = {}
            self.request.session.save()
        carrinho = self.request.session['carinho']
        if variacao_id in carrinho:
             quantidade_carinho = carrinho[variacao_id]['quantidade']
             quantidade_carinho += 1
             if variacao_estoque < quantidade_carinho:
                 messages.warning(
                     self.request,
                     f'Estoque insuficiente para {quantidade_carinho}x no '
                     f'produto "{produto_nome}". Adcionamos {variacao_estoque}x'
                     f'no seu carinho,'
                 )
                 quantidade_carinho = variacao_estoque

             carrinho[variacao_id]['quantidade'] = quantidade_carinho
             carrinho[variacao_id]['preco_quantitativo'] = preco_unitario * \
                quantidade_carinho
             carrinho[variacao_id]['reco_quantitativo_promocianal'] = preco_unitario_promocianal * \
                quantidade_carinho

        else:
             carrinho[variacao_id] = {
                'produto_id': produto.id,
                'produto_nome':  produto.nome,
                'variacao_nome':variacao_nome,
                'variacao_id' :variacao_id,
                'preco_unitario':preco_unitario,
                'preco_unitario_promocianal':preco_unitario_promocianal,
                'preco_quantitativo': preco_unitario,
                'preco_quantitativo_promocianal': preco_unitario_promocianal,
                'quantidade' :1,
                'slug':slug,
                'imagem':imagem,
             }
        self.request.session.save()
        messages.success(
           self.request,
           f'Produto {produto_nome} {variacao_nome} adcionado ao seu '
           f'carrinho{carrinho[variacao_id]["quantidade"]}x.'
       )

        return redirect(http_referer)
class RemoverDoCarinho(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
             return redirect(http_referer)
        if not self.request.session.get('carinho'):
            return redirect(http_referer)
        if variacao_id not in self.request.session['carinho']:
            return redirect(http_referer)
        carinho = self.request.session['carinho'][variacao_id]
        messages.success(
            self.request,
            f'Produto {carinho["produto_nome"]} {carinho["variacao_nome"]} removido do seu carinho.'
        )

        del self.request.session['carinho'] [variacao_id]
        self.request.session.save()
        return redirect(http_referer)


class Carinho(View):
    def get(self,*args,**kwargs):
       contexto ={
        'carinho':self.request.session.get('carinho',{})
    }
       return render(self.request,'produto/carrinho.html',contexto)
class ResumoDacompra(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')


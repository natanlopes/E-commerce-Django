from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('<slug>', views.DetalheProduto.as_view(), name='detalhe'),
    path('adcionaraocarinho/', views.AdcionarAoCarinho.as_view(), name='adcionaraocarinho'),
    path('removerdocarinho/', views.RemoverDoCarinho.as_view(), name='removerdocarinho'),
    path('carinho/', views.Carinho.as_view(), name='carinho'),
    path('resumodacompra/', views.ResumoDacompra.as_view(), name='resumodacompra'),
]

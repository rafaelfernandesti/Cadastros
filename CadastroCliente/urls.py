from django.urls import path
from CadastroCliente import views
#lista urlpatterns global do projeto
urlpatterns = [
    path('', views.index, name = "index"),
    path('clientes/', views.listar_clientes, name = "clientes"),
]
from django.urls import path
from CadastroCliente import views
#lista urlpatterns global do projeto
urlpatterns = [
    path('', views.index, name = "index"),
]
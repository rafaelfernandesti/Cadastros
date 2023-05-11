from django.shortcuts import render
from CadastroCliente.models import Cliente, Profissao
# Create your views here.
def index(request):
    meu_nome = "Rafael Fernandes"
    lista_frutas = ['Laranja','Maçã','Uva','Banana']
    context = {
        'nome':meu_nome,
        'frutas':lista_frutas
    }
    return render(request, 'index.html',context)

def listar_clientes(request): #sempre insira o request como parâmetro aqui
    lista_clientes = Cliente.objects.all() # essa linha faz a seleção no banco de dados para retornar os valores
    lista_profissoes = Profissao.objects.all()
    #o dicionário (variavel) context é o que vi para para o template
    context = {
        "clientes":lista_clientes,
        "profissoes": lista_profissoes,
    }
    return render(request, 'lista_clientes.html', context)
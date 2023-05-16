from django.shortcuts import render
from CadastroCliente.models import Cliente, Profissao, Telefone
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

def detalhar_cliente(request, id):
    #buscando no banco de dados o cliente pelo id
    cliente = Cliente.objects.get(id = id)
    telefones = Telefone.objects.filter(id_cliente_id = id) #adicionamos esta linha para obter todos os telefones de um cliente específico
    context = {
        "cliente": cliente,
        "telefones":telefones
    }
    return render(request, "cliente_detalhes.html", context)
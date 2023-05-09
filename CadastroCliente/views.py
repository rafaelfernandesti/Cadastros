from django.shortcuts import render

# Create your views here.
def index(request):
    meu_nome = "Rafael Fernandes"
    lista_frutas = ['Laranja','Maçã','Uva','Banana']
    context = {
        'nome':meu_nome,
        'frutas':lista_frutas
    }
    return render(request, 'index.html',context)
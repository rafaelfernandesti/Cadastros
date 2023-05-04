from django.contrib import admin
from CadastroCliente.models import Cliente
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    #colunas exibidas
    list_display = ['id','nome','telefone','cidade']
    #colunas clicáveis
    list_display_links = ['id']
    #filtros
    list_filter = ['bairro','cidade','ativo']
    #campo editável
    list_editable = ['nome']

admin.site.register(Cliente, ClienteAdmin)

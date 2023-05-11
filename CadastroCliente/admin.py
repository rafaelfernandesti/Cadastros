from django.contrib import admin
from CadastroCliente.models import Cliente, Profissao, Telefone
# Register your models here.

class Telefones(admin.StackedInline):
    model = Telefone
    extra = 4

class ClienteAdmin(admin.ModelAdmin):
    #colunas exibidas
    list_display = ['id','nome','cidade']
    #colunas clicáveis
    list_display_links = ['id']
    #filtros
    list_filter = ['bairro','cidade','ativo']
    #campo editável
    #list_editable = ['nome']
    inlines = [Telefones]


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Telefone)
admin.site.register(Profissao)

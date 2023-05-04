from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    nro = models.IntegerField(blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    matricula = models.IntegerField()
    renda_mensal = models.DecimalField(max_digits=10,decimal_places=2)
    ativo = models.BooleanField()
    foto = models.ImageField()

    #a função abaixo serve para sobrescrever a função original e exibir na listagem o nome do cliente
    def __str__(self):
        return self.nome

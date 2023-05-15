from django.db import models
class Profissao(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Profissões"

    #a função abaixo serve para sobrescrever a função original str e exibir na listagem o nome do cliente
    def __str__(self):
        return self.nome

# Create your models here.
class Cliente(models.Model):
    ESTADO_CIVIL = [
        ('SOL','Solteiro'),
        ('CAS','Casado'),
        ('DIV','Divorciado'),
        ('VIU','Viúvo')
    ]
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    #telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    nro = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    matricula = models.IntegerField()
    renda_mensal = models.DecimalField(max_digits=10,decimal_places=2)
    ativo = models.BooleanField()
    estado_civil = models.CharField(max_length=3, choices=ESTADO_CIVIL, null=True)
    profissao = models.ForeignKey(
        Profissao,on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Profissão"
    )

class Telefone(models.Model):
    ddd = models.CharField(max_length=2)
    numero = models.CharField(max_length=10)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return f"({self.ddd}) {self.numero}"

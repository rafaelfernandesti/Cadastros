# Generated by Django 4.2 on 2023-04-20 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroCliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='bairro',
            field=models.CharField(default='teste', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='cep',
            field=models.CharField(default='00000-000', max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='cidade',
            field=models.CharField(default='São Paulo', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(default='Rua', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='nro',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.12 on 2023-02-04 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Formulario_de_Amostra',
            new_name='FormularioDeAmostra',
        ),
        migrations.RenameModel(
            old_name='Lista_de_Servico',
            new_name='ListaDeServico',
        ),
        migrations.RenameModel(
            old_name='Solicitacao_de_Servico',
            new_name='SolicitacaoDeServico',
        ),
    ]

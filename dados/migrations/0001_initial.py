# Generated by Django 3.2.12 on 2023-02-04 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista_de_Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_parametro', models.CharField(help_text='nome do agente químico', max_length=100)),
                ('unidade_de_medida_do_parametro', models.CharField(help_text='unidade de medida do agente químico', max_length=10)),
                ('resultado', models.CharField(help_text='valor mensurado do agente químico na amostra', max_length=10)),
                ('lq', models.CharField(help_text='valor de referência', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitacao_de_Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=200)),
                ('empresa_avaliada', models.CharField(max_length=200)),
                ('lugar_de_coleta', models.CharField(max_length=200)),
                ('formulario_de_amostra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dados.parametro')),
            ],
        ),
        migrations.CreateModel(
            name='Formulario_de_Amostra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_solicitacao_de_serviço', models.CharField(max_length=200)),
                ('tipo_de_amostra', models.CharField(max_length=200)),
                ('data_de_coleta', models.DateField()),
                ('amostra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dados.parametro')),
            ],
        ),
        migrations.CreateModel(
            name='Amostra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_interno', models.CharField(help_text='Código de identificação interna ACME', max_length=50)),
                ('setor_local_avaliado', models.CharField(max_length=100)),
                ('hora_da_coleta', models.CharField(max_length=100)),
                ('data_da_coleta', models.DateField()),
                ('metodo_de_analise', models.CharField(max_length=100)),
                ('descricao_do_metodo', models.CharField(max_length=100)),
                ('data_de_entrada_no_laboratorio', models.DateField()),
                ('data_do_relatorio_de_ensaio', models.DateField()),
                ('unidade_de_medida', models.CharField(max_length=100)),
                ('volume', models.CharField(max_length=10)),
                ('conclusao', models.CharField(max_length=200)),
                ('observacao', models.CharField(max_length=200)),
                ('irregularidades', models.CharField(max_length=200)),
                ('parametro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dados.parametro')),
            ],
        ),
    ]
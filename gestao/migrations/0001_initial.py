# Generated by Django 2.0.4 on 2018-05-23 14:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('planotrabalho', '0001_initial'),
        ('adesao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diligencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_diligencia', models.TextField(max_length=200)),
                ('data_criacao', models.DateField(default=datetime.date.today)),
                ('componente_id', models.PositiveIntegerField()),
                ('tipo_diligencia', models.CharField(choices=[('geral', 'Geral'), ('componente', 'Específica')], max_length=10)),
                ('classificacao_arquivo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planotrabalho.SituacoesArquivoPlano')),
                ('componente_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('ente_federado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adesao.Municipio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adesao.Usuario')),
            ],
        ),
    ]

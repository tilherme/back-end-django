# Generated by Django 3.2.6 on 2021-08-31 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0001_initial'),
        ('core', '0004_pontos_turisticos_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontos_turisticos',
            name='avalicoes',
            field=models.ManyToManyField(to='avaliacao.Avaliacao'),
        ),
    ]

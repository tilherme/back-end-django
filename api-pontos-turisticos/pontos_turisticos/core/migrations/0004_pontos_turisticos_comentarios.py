# Generated by Django 3.2.6 on 2021-08-31 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0001_initial'),
        ('core', '0003_pontos_turisticos_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontos_turisticos',
            name='comentarios',
            field=models.ManyToManyField(to='comentario.Comentario'),
        ),
    ]

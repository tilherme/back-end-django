# Generated by Django 3.2.6 on 2021-08-29 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontos_turisticos',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]

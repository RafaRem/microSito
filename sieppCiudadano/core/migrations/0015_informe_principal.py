# Generated by Django 2.2.13 on 2020-09-29 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_eje_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='informe',
            name='principal',
            field=models.CharField(max_length=500, null=True, verbose_name='Eje que se mostrara primero'),
        ),
    ]

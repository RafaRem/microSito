# Generated by Django 2.2.13 on 2020-07-31 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200731_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacionespecial',
            old_name='epecial',
            new_name='especial',
        ),
        migrations.AddField(
            model_name='galeriasub',
            name='especial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Especial', verbose_name='Evento Especial'),
        ),
    ]

# Generated by Django 2.2.13 on 2020-10-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_informe_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eje',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Video Promocional'),
        ),
    ]

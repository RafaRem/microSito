# Generated by Django 2.2.13 on 2020-10-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20201029_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informe',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Video Promocional'),
        ),
    ]

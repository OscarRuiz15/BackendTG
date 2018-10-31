# Generated by Django 2.1 on 2018-10-21 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0003_auto_20181002_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='fecha_visita',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visita',
            name='hora_visita',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
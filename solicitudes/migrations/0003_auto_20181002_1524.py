# Generated by Django 2.1 on 2018-10-02 20:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_auto_20181002_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='email',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), size=None),
        ),
    ]

# Generated by Django 2.1 on 2019-03-30 19:03

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0002_auto_20190204_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='{}', max_length=100), size=None)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
            ],
        ),
    ]

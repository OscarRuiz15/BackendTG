# Generated by Django 2.1 on 2019-07-07 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0005_auto_20190601_0130'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecomendacionLugares',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.CharField(max_length=100)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lugares.Lugar')),
            ],
        ),
    ]

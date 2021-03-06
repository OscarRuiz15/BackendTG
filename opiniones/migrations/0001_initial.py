# Generated by Django 2.1 on 2019-03-20 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0002_auto_20190204_2158'),
        ('lugares', '0002_auto_20190319_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('like', models.BooleanField(default=False)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lugares.Lugar')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
            ],
        ),
    ]

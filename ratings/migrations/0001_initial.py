# Generated by Django 2.1 on 2018-11-09 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lugares', '0006_auto_20181104_2009'),
        ('usuarios', '0002_usuario_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lugares.Lugar')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
            ],
        ),
    ]
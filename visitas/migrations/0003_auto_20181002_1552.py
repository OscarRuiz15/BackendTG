# Generated by Django 2.1 on 2018-10-02 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0003_lugar_propietario'),
        ('usuarios', '0002_usuario_uid'),
        ('visitas', '0002_auto_20180930_0141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visita',
            name='lugar',
        ),
        migrations.AddField(
            model_name='visita',
            name='lugar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lugares.Lugar'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='visita',
            name='usuario',
        ),
        migrations.AddField(
            model_name='visita',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
            preserve_default=False,
        ),
    ]

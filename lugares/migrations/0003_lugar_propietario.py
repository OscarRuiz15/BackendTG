# Generated by Django 2.1 on 2018-10-02 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_uid'),
        ('lugares', '0002_auto_20181002_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='propietario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
            preserve_default=False,
        ),
    ]

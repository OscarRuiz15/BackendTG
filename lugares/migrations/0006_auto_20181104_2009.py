# Generated by Django 2.1 on 2018-11-05 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0005_auto_20181003_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='comentario',
            field=models.ManyToManyField(blank=True, to='comentarios.Comentario'),
        ),
    ]

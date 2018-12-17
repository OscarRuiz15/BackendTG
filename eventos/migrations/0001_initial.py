# Generated by Django 2.1 on 2018-12-17 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comentarios', '0001_initial'),
        ('lugares', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=100)),
                ('foto', models.CharField(max_length=100)),
                ('calificacion', models.DecimalField(decimal_places=1, max_digits=2)),
                ('tipo', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('finalizado', models.BooleanField(default=False)),
                ('comentario', models.ManyToManyField(blank=True, to='comentarios.Comentario')),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lugares.Lugar')),
            ],
        ),
    ]

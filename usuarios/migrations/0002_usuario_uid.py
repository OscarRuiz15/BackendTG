# Generated by Django 2.1 on 2018-09-26 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='uid',
            field=models.CharField(default='eg', max_length=100),
            preserve_default=False,
        ),
    ]

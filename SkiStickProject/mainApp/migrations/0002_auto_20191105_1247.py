# Generated by Django 2.2.6 on 2019-11-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacion',
            name='alturaMaxima',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='estacion',
            name='alturaMinima',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='estacion',
            name='kmsPista',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='estacion',
            name='numeroRemontes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='estaciontotipopista',
            name='numeroPistas',
            field=models.IntegerField(),
        ),
    ]

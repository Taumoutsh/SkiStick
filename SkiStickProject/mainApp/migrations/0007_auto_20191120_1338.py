# Generated by Django 2.0 on 2019-11-20 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_auto_20191120_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estaciontousuario',
            name='fecha',
            field=models.TextField(),
        ),
    ]

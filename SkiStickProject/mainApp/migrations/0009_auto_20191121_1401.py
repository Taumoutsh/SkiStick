# Generated by Django 2.0 on 2019-11-21 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_auto_20191121_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estaciontousuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
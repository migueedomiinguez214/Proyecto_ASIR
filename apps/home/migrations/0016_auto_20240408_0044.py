# Generated by Django 3.2.6 on 2024-04-07 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20240407_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito_1',
            name='Die_Aler_Otro_cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carrito_1',
            name='General_cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carrito_1',
            name='Otros_cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carrito_1',
            name='Postres_cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carrito_1',
            name='Sal_cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 3.2.6 on 2024-04-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_articulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('General', models.CharField(max_length=100)),
                ('Die_Aler_Otro', models.CharField(max_length=100)),
                ('Sal', models.BooleanField()),
                ('Postres_Extra', models.CharField(max_length=100)),
                ('Otros', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Articulo',
        ),
    ]
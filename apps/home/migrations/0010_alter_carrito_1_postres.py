# Generated by Django 3.2.6 on 2024-04-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20240405_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito_1',
            name='Postres',
            field=models.CharField(choices=[('Yogurt', 'Yogurt'), ('Fruta', 'Fruta'), ('Papilla de fruta', 'Papilla de fruta')], max_length=100),
        ),
    ]

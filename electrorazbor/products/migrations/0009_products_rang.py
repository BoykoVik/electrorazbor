# Generated by Django 5.0.4 on 2024-11-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_products_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='rang',
            field=models.IntegerField(default=1, verbose_name='Порядок вывода'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-10-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(related_name='products', to='products.categories', verbose_name='Вид товара'),
        ),
    ]

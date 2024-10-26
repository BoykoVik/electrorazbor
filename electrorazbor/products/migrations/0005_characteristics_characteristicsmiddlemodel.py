# Generated by Django 5.0.4 on 2024-10-26 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_cost_products_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350, unique=True, verbose_name='Наименование характеристики')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CharacteristicsMiddleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(blank=True, max_length=1500, null=True, verbose_name='Показатель')),
                ('characteristic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.characteristics', verbose_name='Характеристика')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='products.products', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Показатель',
                'verbose_name_plural': 'Показатели',
                'ordering': ['id'],
            },
        ),
    ]
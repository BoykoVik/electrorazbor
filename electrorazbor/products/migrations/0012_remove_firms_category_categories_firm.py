# Generated by Django 5.0.4 on 2025-01-25 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_categories_firm_firms_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firms',
            name='category',
        ),
        migrations.AddField(
            model_name='categories',
            name='firm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='firm', to='products.firms', verbose_name='Фирма'),
        ),
    ]

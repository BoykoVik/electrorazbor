# Generated by Django 5.0.4 on 2024-10-26 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_products_keywords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='keywords',
        ),
    ]

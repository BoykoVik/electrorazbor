# Generated by Django 5.0.4 on 2024-11-10 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_categories_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='show',
            field=models.BooleanField(default=True, verbose_name='В наличии?'),
        ),
    ]

# Generated by Django 5.0.4 on 2025-01-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_firms_categories_image_categories_firm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='firm',
        ),
        migrations.AddField(
            model_name='firms',
            name='category',
            field=models.ManyToManyField(related_name='firm', to='products.categories', verbose_name='Фирма'),
        ),
    ]

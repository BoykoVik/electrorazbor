# Generated by Django 5.0.4 on 2024-10-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'ordering': ['ranc'], 'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AddField(
            model_name='contacts',
            name='ranc',
            field=models.IntegerField(default=1, verbose_name='Порядок вывода'),
        ),
    ]

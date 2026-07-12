# update_ratings.py
import random
from django.core.management.base import BaseCommand
from products.models import Products  # замените your_app на имя вашего приложения

class Command(BaseCommand):
    help = 'Обновляет рейтинги всех товаров случайными значениями от 4.5 до 4.9'

    def handle(self, *args, **options):
        products = Products.objects.all()
        count = 0
        
        for product in products:
            # Генерируем случайное число от 4.5 до 4.9 с шагом 0.01
            rating = round(random.uniform(4.5, 4.9), 2)
            product.rating = rating
            product.save()
            count += 1
            
            if count % 100 == 0:
                self.stdout.write(f'Обновлено {count} товаров')
        
        self.stdout.write(
            self.style.SUCCESS(f'Успешно обновлены рейтинги для {count} товаров')
        )

import random
from products.models import Products

products = Products.objects.all()
for product in products:
    product.rating = round(random.uniform(4.5, 4.9), 2)
    product.save()
    print(f'Обновлен рейтинг для {product.name}: {product.rating}')
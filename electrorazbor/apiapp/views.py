from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
from products.models import Orders, Obtains, Products
from coreapp.utils import tgsandmsg

def createorder(request):
    if request.method == 'POST':
        try:
            # Парсим JSON-тело запроса
            data = json.loads(request.body)
            phone = data.get('phone')
            cart = data.get('cart')
            textmessage = data.get('textmessage')
            
            # Проверяем, что телефон и корзина переданы
            if not phone or not cart:
                return JsonResponse({'error': 'Необходимо указать телефон и корзину'}, status=400)

            # Логика создания заказа
            order = create_order_in_db(phone, cart)
            if textmessage:
                tgsandmsg(f'НОВЫЙ ЗАКАЗ номер {order.id}\nКомментарий к заказу:\n{textmessage}')
            else:
                tgsandmsg(f'НОВЫЙ ЗАКАЗ номер {order.id}\n')
            # Возвращаем успешный ответ с номером заказа
            return JsonResponse({'order_id': order.id})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Неверный формат JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # Если метод не POST, возвращаем ошибку
    return JsonResponse({'error': 'Метод не поддерживается'}, status=405)

def create_order_in_db(phone, cart):
    """
    Создает заказ в базе данных и возвращает объект заказа.
    """
    # Создаем заказ
    order = Orders.objects.create(phone=phone)
    
    #order.save()
    # Добавляем товары из корзины в заказ
    for item in cart:
        obtain = Obtains()
        obtain.order = order
        prod = get_object_or_404(Products, pk = int(item['id']))#ТОВАР
        obtain.product = prod
        obtain.count = item['quantity']
        obtain.save()
    return order
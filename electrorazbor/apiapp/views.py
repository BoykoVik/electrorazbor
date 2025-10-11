from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
from products.models import Orders, Obtains, Products
from coreapp.utils import tgsandmsg
from coreapp.models import Callrequest, Pricerequest

def createorder(request):
    if request.method == 'POST':
            try:
                phone = request.POST.get('phone', '')
                textmessage = request.POST.get('textmessage', '')
                
                # Выводим данные в консоль сервера
                print(f"Получена заявка на прайс:")
                print(f"Телефон: {phone}")
                print(f"Сообщение: {textmessage}")
                
                # Возвращаем успешный ответ
                return JsonResponse({'success': True})
                
            except Exception as e:
                print(f"Ошибка при обработке формы: {e}")
                return JsonResponse({'success': False})
        
    return JsonResponse({'success': False})

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

def mark_callrequest_called(request, callrequest_id, type):
    try:
        if type == "call":
            callrequest = Callrequest.objects.get(id=callrequest_id)
        elif type== "price":
            callrequest = Pricerequest.objects.get(id=callrequest_id)
        callrequest.is_called = True
        callrequest.save()
        return JsonResponse({'status': 'success'}, status=200)
    except Callrequest.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Callrequest not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    

def toggle_order_status(request, order_id):
    try:
        order = Orders.objects.get(id=order_id)
        data = json.loads(request.body)
        order.is_called = data.get('is_called', False)
        order.save()
        return JsonResponse({
            'status': 'success',
            'is_called': order.is_called,
            'new_text': '✅ отработано' if order.is_called else '❌ не отработано'
        })
    except Orders.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Order not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
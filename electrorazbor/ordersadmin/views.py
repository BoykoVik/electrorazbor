from django.shortcuts import render, get_object_or_404
from products.models import Products, Orders, Obtains
from coreapp.models import Callrequest, Pricerequest, Holdmerequest
from django.db.models import Sum, F
from django.http import HttpResponseForbidden, JsonResponse
from django.views.decorators.http import require_POST
import json
from django.core.paginator import Paginator

def orderslist(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Доступ запрещен")
    
    # Базовый запрос с аннотацией суммы
    orders = Orders.objects.annotate(
        total_price=Sum(F('order__product__price') * F('order__count'))
    )
    
    # Получаем параметр фильтра из GET-запроса
    status_filter = request.GET.get('status', 'all')
    
    # Применяем фильтр
    if status_filter == 'new':
        orders = orders.filter(is_called=False)
    elif status_filter == 'processed':
        orders = orders.filter(is_called=True)
    # 'all' - без фильтрации
    
    # Сортируем по ID (сначала новые)
    orders = orders.order_by('-id')
    
    # Считаем общее количество для статистики (без пагинации)
    total_count = Orders.objects.count()
    new_count = Orders.objects.filter(is_called=False).count()
    processed_count = Orders.objects.filter(is_called=True).count()
    
    # Пагинация (25 заказов на страницу)
    paginator = Paginator(orders, 25)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    
    # Проверяем AJAX-запрос для фильтрации
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Возвращаем только HTML контейнера с заказами и пагинацию
        return render(request, 'ordersadmin/orderslist_ajax.html', {
            'orders': page.object_list,
            'page': page,
            'current_status': status_filter,
        })
    
    return render(request, 'ordersadmin/orderslist.html', {
        'title': 'Список заказов',
        'description': 'админка',
        'callrequests': Callrequest.objects.all().order_by('-id'),
        'pricerequests': Pricerequest.objects.all().order_by('-id'),
        'holdrequests': Holdmerequest.objects.all().order_by('-id'),
        'orders': page.object_list,
        'page': page,
        'current_status': status_filter,
        'total_count': total_count,
        'new_count': new_count,
        'processed_count': processed_count,
    })

def orderdetail(request, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Доступ запрещен")
    order = get_object_or_404(Orders, id=id)
    obtains = Obtains.objects.filter(order=order.id)
    total_sum = sum(obtain.product.price * obtain.count for obtain in obtains)
    return render(request, 'ordersadmin/orderdetail.html', {
        'order': order,
        'obtains': obtains,
        'total_sum': total_sum,
        'title': f'Заказ #{order.id}',
        'description': 'админка',
    })

@require_POST
def update_order_comment(request):
    if not request.user.is_superuser:
        return JsonResponse({'error': 'Доступ запрещен'}, status=403)
    
    try:
        data = json.loads(request.body)
        order_id = data.get('order_id')
        comment = data.get('comment', '').strip()
        
        order = get_object_or_404(Orders, id=order_id)
        order.comment = comment
        order.save()
        
        return JsonResponse({
            'success': True,
            'comment': order.comment,
            'comment_date': order.comment_date.strftime('%d.%m.%Y %H:%M')
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_POST
def toggle_order_status(request):
    if not request.user.is_superuser:
        return JsonResponse({'error': 'Доступ запрещен'}, status=403)
    
    try:
        data = json.loads(request.body)
        order_id = data.get('order_id')
        
        order = get_object_or_404(Orders, id=order_id)
        order.is_called = not order.is_called
        order.save()
        
        return JsonResponse({
            'success': True,
            'is_called': order.is_called
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
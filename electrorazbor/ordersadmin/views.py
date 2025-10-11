from django.shortcuts import render, get_object_or_404
from products.models import Products, Orders, Obtains
from coreapp.models import Callrequest, Pricerequest
from django.db.models import Sum, F
from django.http import HttpResponseForbidden
# Create your views here.
def orderslist(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Доступ запрещен")
    callreqs = Callrequest.objects.all().order_by('-id')
    pricereqs = Pricerequest.objects.all().order_by('-id')
    orders = Orders.objects.annotate(total_price=Sum(F('order__product__price') * F('order__count'))).order_by('-id')
    return render(request, 'ordersadmin/orderslist.html', {
        'title': 'Список заказов',
        'description': 'админка',
        'callrequests': callreqs,
        'pricerequests': pricereqs,
        'orders': orders,
    })

def orderdetail(request, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Доступ запрещен")
    order = get_object_or_404(Orders, id = id)
    obtains = Obtains.objects.filter(order = order.id)
    total_sum = sum(obtain.product.price * obtain.count for obtain in obtains)
    return render(request, 'ordersadmin/orderdetail.html', {
    'order': order,
    'obtains': obtains,
    'total_sum': total_sum,
    'title': f'Заказ #{order.id}',
    'description': 'админка',
    })

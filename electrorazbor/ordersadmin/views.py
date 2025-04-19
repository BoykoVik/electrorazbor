from django.shortcuts import render, get_object_or_404
from products.models import Products, Orders, Obtains
from coreapp.models import Callrequest
from django.db.models import Sum, F
# Create your views here.
def orderslist(request):
    callreqs = Callrequest.objects.all()
    orders = Orders.objects.annotate(total_price=Sum(F('order__product__price') * F('order__count'))).all()
    return render(request, 'ordersadmin/orderslist.html', {
        'title': 'Список заказов',
        'description': 'админка',
        'callrequests': callreqs,
        'orders': orders,
    })

def orderdetail(request, id):
    order = get_object_or_404(Orders, id = id)
    obtains = Obtains.objects.filter(order = order.id)
    return render(request, 'ordersadmin/orderdetail.html', {
    'order': order,
    'obtains': obtains,
    'title': f'Заказ #{order.id}',
    'description': 'админка',
    })

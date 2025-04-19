from django.shortcuts import render, get_object_or_404
from products.models import Products, Orders, Obtains
from coreapp.models import Callrequest
# Create your views here.
def orderslist(request):
    callreqs = Callrequest.objects.all()
    orders = Orders.objects.all()
    return render(request, 'ordersadmin/orderslist.html', {
        'title': 'Список заказов',
        'description': 'админка',
        'callrequests': callreqs,
        'orders': orders,
    })
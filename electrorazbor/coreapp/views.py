from django.shortcuts import render
from products.models import Categories, Products
from .models import Contacts, Callrequest
from django.http import JsonResponse
from .utils import tgsandmsg
# Create your views here.
def home(request):
    return render(request, 'coreapp/home.html', {
        'models': Categories.objects.all(),
        'products': Products.objects.filter(in_top=True),
        'title': 'Запчасти для электросамокатов. Недорого.',
        'description': 'Продажа запчастей для электросамокатов. Помощь в подборе. Доставка.',
        'contacts': Contacts.objects.all(),
    })

def contacts(request):
    return render(request, 'coreapp/contacts.html', {
        'models': Categories.objects.all(),
        'title': 'Контакты. Запчасти для электросамокатов. Недорого.',
        'description': 'Контакты. Продажа запчастей для электросамокатов. Помощь в подборе. Доставка.',
        'contacts': Contacts.objects.all(),
    })

def productrequest(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        product = request.POST.get('product')
        req = Callrequest()
        req.number = phone
        req.product = product
        req.save()
        tgsandmsg(f'Заявка! \nТелефон {phone}\nТовар: {product}')
    return JsonResponse({"OK":'200'})
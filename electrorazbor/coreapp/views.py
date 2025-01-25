from django.shortcuts import render
from products.models import Categories, Products, Firms
from .models import Contacts, Callrequest
from django.http import JsonResponse
from django.views.generic import TemplateView
from .utils import tgsandmsg
# Create your views here.
def home(request):
    return render(request, 'coreapp/home.html', {
        'firms': Firms.objects.all(),
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

class RobotsTxtView(TemplateView):
    template_name = 'coreapp/robots.txt'
    content_type = 'text/plain'

class SitemapXmlView(TemplateView):
    template_name = 'coreapp/sitemap.xml'
    content_type = 'application/xml'

    def get_context_data(self, **kwargs):
        products = Products.objects.all()
        categories = Categories.objects.all()
        firms = Firms.objects.all()
        return {
            'products': products,
            'categories': categories,
            'firms': firms,
        }
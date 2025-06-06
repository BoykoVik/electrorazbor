from django.shortcuts import render
from products.models import Categories, Products, Firms
from .models import Contacts, Callrequest
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.db.models import Q
from .utils import tgsandmsg
import datetime
# Create your views here.
def home(request):
    return render(request, 'coreapp/home.html', {
        'firms': Firms.objects.all(),
        'products': Products.objects.filter(in_top=True),
        'title': 'Комплектующие и запчасти для электросамокатов Ninebot и Xiaomi. Недорого.',
        'description': 'Купить запчасти и комплектующие для электросамокатов от компании Electrorazbor - тормозные диски и колодки, колеса, поворотники, фары, ручки, амортизаторы купить в Москве, цена и фото каждого товара. Заказ онлайн. Быстрая доставка.',
        'contacts': Contacts.objects.all(),
    })

def contacts(request):
    return render(request, 'coreapp/contacts.html', {
        'models': Categories.objects.all(),
        'title': 'Контакты. Запчасти для электросамокатов Ninebot и Xiaomi. Недорого.',
        'description': 'Контакты. Продажа запчастей для электросамокатов. Помощь в подборе. Доставка.',
        'contacts': Contacts.objects.all(),
    })

def delivery(request):
    return render(request, 'coreapp/delivery.html', {
        'title': 'Доставка и самовывоз. Запчасти для электросамокатов Ninebot и Xiaomi. Недорого.',
        'description': 'Доставка и самовывоз запчастей и комплектующих для электросамокатов Ninebot и Xiaomi',
        'contacts': Contacts.objects.all(),
    })

def uslovija_vozvrata(request):
    return render(request, 'coreapp/uslovija_vozvrata.html', {
        'title': 'Условия возврата и обмена. Запчасти для электросамокатов Ninebot и Xiaomi. Недорого.',
        'description': 'Условия возврата и обмена запчастей и комплектующих для электросамокатов Ninebot и Xiaomi',
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

def cart(request):
    return render(request, 'coreapp/cart.html', {
        'firms': Firms.objects.all(),
        'products': Products.objects.filter(in_top=True),
        'title': 'Корзина | Запчасти для электросамокатов Ninebot и Xiaomi. Недорого.',
        'description': 'Корзина | Продажа запчастей для электросамокатов. Помощь в подборе. Доставка.',
        #'contacts': Contacts.objects.all(),
    })

def soglasie(request):
    return render(request, 'coreapp/soglasie.html', {
        'firms': Firms.objects.all(),
        'products': Products.objects.filter(in_top=True),
        'title': 'Согласие на обработку персональных данных | Запчасти для электросамокатов Ninebot и Xiaomi. Недорого.',
        'description': 'Согласие на обработку персональных данных | Продажа запчастей для электросамокатов. Помощь в подборе. Доставка.',
        'contacts': Contacts.objects.all(),
    })

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
    
def page_not_found_view(request, exception):
    return render(request, 'coreapp/404.html', {
        'firms': Firms.objects.all(),
        'products': Products.objects.filter(in_top=True),
        'title': '404 - страница не найдена',
        'description': '404 - страница не найдена',
        'contacts': Contacts.objects.all(),
        },
         status=404,)

def search(request):
    search_query = request.GET.get('query')
    print(search_query)
    if search_query:
        products = Products.objects.filter(Q(name__iregex=search_query))
    else:
        products = []
    return render(request, 'coreapp/search.html', {
        'firms': Firms.objects.all(),
        'products': products,
        'title': f'Поиск по сайту | {search_query} | Запчасти для электросамокатов. Недорого.',
        'description': 'Поиск по сайту | {search_query} | Продажа запчастей для электросамокатов. Помощь в подборе. Доставка.',
        'contacts': Contacts.objects.all(),
        })

class FeedymlView(TemplateView):
    template_name = 'feed.yml'
    content_type = 'application/xml'

    def get_context_data(self, **kwargs):
        products = Products.objects.filter(use_in_feed=True)
        return {
            'products': products,
            'currentdate': datetime.date.today().isoformat()
        }
    
class FeedxmlView(TemplateView):
    template_name = 'googlefeed.xml'
    content_type = 'application/xml'

    def get_context_data(self, **kwargs):
        products = Products.objects.filter(use_in_feed=True, show=True)
        return {
            'products': products,
        }
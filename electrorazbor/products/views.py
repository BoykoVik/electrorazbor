from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Categories, Products
from coreapp.models import Contacts
# Create your views here.

def productdetail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, 'products/product-detail.html', {
        'title': 'Кухни на заказ от moskitchens.ru. ' + product.name,
        'description': product.desctiption,
        'keywords': product.keywords,
        'product': product,
        'models': Categories.objects.all(),
        'contacts': Contacts.objects.all(),
    })

def products_category(request, slug):
    category = get_object_or_404(Categories, slug=slug)
    products = Products.objects.filter(category=category)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    paginator = Paginator(products, 12)
    page = paginator.get_page(page_num)
    return render(request, 'products/shop-list.html', {
        'title': 'Кухни на заказ от moskitchens.ru. ' + category.name,
        'description': category.desctiption,
        'keywords': category.keywords,
        'products': page.object_list,
        'models': Categories.objects.all(),
        'contacts': Contacts.objects.all(),
        'page': page,
    })
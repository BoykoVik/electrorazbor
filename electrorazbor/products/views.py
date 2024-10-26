from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Categories, Products
from coreapp.models import Contacts
# Create your views here.

def productdetail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, 'products/product-detail.html', {
        'title': product.name + ' купить. Запчасти для электросамокатов',
        'description': product.desctiption,
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
        'title': category.name + '. Купить. Запчасти для электросамокатов',
        'description': category.desctiption,
        'products': page.object_list,
        'models': Categories.objects.all(),
        'contacts': Contacts.objects.all(),
        'page': page,
    })
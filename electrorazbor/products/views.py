from django.shortcuts import render, get_object_or_404
from .models import Categories, Products
# Create your views here.

def products_category(request, slug):
    category = get_object_or_404(Categories, slug=slug)
    return render(request, 'products/shop-grid.html', {
        'title': 'Кухни на заказ от moskitchens.ru. ' + category.name,
        'description': category.desctiption,
        'keywords': category.keywords,
        'products': Products.objects.filter(category=category),
        'categories': Categories.objects.all(),
    })
from django.shortcuts import render
from products.models import Categories, Products

# Create your views here.
def home(request):
    return render(request, 'coreapp/home.html', {
        'models': Categories.objects.all(),
        'products': Products.objects.all(),
        'title': '',
        'description': '',
        'keywords': '',
    })
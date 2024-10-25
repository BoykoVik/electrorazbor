from django.shortcuts import render
from products.models import Categories, Products
from .models import Contacts
# Create your views here.
def home(request):
    return render(request, 'coreapp/home.html', {
        'models': Categories.objects.all(),
        'products': Products.objects.filter(in_top=True),
        'title': '',
        'description': '',
        'keywords': '',
        'contacts': Contacts.objects.all(),
    })
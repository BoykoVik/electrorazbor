from django.shortcuts import render
from products.models import Categories

# Create your views here.
def home(request):
    return render(request, 'coreapp/home.html', {
        'models': Categories.objects.all(),
        'title': '',
        'description': '',
        'keywords': '',
    })
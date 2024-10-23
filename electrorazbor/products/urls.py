from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    #path('<slug:slug>/', views.productdetail, name='productdetail'),
    path('categories/<slug:slug>/', views.products_category, name='products_category'),
    
]
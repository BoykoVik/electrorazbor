from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    path('<slug:slug>/', views.productdetail, name='productdetail'),
    path('firms/<slug:slug>/', views.firms_category, name='firms_category'),
    path('<slug:firm>/<slug:slug>/', views.products_category, name='products_category'),
]
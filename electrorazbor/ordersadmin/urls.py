from django.urls import path
from . import views
app_name = 'ordersadmin'

urlpatterns = [
    path('', views.orderslist, name='orderslist'),
]
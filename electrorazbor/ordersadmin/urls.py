from django.urls import path
from . import views
app_name = 'ordersadmin'

urlpatterns = [
    path('', views.orderslist, name='orderslist'),
    path('orderdetail/<int:id>', views.orderdetail, name='orderdetail'),
    # API-эндпоинты для комментариев и статуса
    path('api/update-comment/', views.update_order_comment, name='update_comment'),
    path('api/toggle-status/', views.toggle_order_status, name='toggle_status'),
]
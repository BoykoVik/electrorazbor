from django.urls import path
from . import views
app_name = 'apiapp'

urlpatterns = [
    path('createorder', views.createorder, name='createorder'),
    path('mark_called/<int:callrequest_id>/', views.mark_callrequest_called, name='mark_callrequest_called'),
    path('orders/<int:order_id>/toggle_status/', views.toggle_order_status, name='toggle_order_status'),
]
from django.urls import path
from . import views
app_name = 'apiapp'

urlpatterns = [
    path('createorder', views.createorder, name='createorder'),
]
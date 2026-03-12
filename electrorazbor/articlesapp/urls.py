from django.urls import path
from . import views
app_name = 'articlesapp'

urlpatterns = [
    path('blog-list/', views.blog_list, name='blog_list'),
    path('<slug:slug>/', views.articledetail, name='articledetail'),
]
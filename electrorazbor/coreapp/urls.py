from django.urls import path
from . import views
from django.views.generic import RedirectView
app_name = 'coreapp'

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('feedyml', views.FeedymlView.as_view()),
    path('robots.txt', views.RobotsTxtView.as_view()),
    path('sitemap.xml', views.SitemapXmlView.as_view()),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('contacts/', views.contacts, name='contacts'),
    path('cart/', views.cart, name='cart'),
    path('favicon.ico', favicon_view),
    path('productrequest/', views.productrequest, name='productrequest'),
]
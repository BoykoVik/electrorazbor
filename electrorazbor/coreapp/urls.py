from django.urls import path
from . import views
from django.views.generic import RedirectView
app_name = 'coreapp'

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    #path('robots.txt', views.RobotsTxtView.as_view()),
    #path('sitemap.xml', views.SitemapXmlView.as_view()),
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    #path('about-us', views.about_us, name='about-us'),
    path('favicon.ico', favicon_view),
    path('productrequest/', views.productrequest, name='productrequest'),
]
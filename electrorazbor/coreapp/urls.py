from django.urls import path
from . import views
from django.views.generic import RedirectView
app_name = 'coreapp'

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('googlefeedxml', views.FeedxmlView.as_view()),
    path('feedyml', views.FeedymlView.as_view()),
    path('robots.txt', views.RobotsTxtView.as_view()),
    path('sitemap.xml', views.SitemapXmlView.as_view()),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('delivery/', views.delivery, name='delivery'),
    path('uslovija_vozvrata/', views.uslovija_vozvrata, name='uslovija_vozvrata'),
    path('contacts/', views.contacts, name='contacts'),
    path('cart/', views.cart, name='cart'),
    path('favicon.ico', favicon_view),
    path('productrequest/', views.productrequest, name='productrequest'),
    path('soglasie-na-obrabotku-personalnih-dannih/', views.soglasie, name='soglasie'),
    path('optivii-price/', views.price_opt, name='price_opt'),
]
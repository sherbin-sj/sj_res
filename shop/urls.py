from django.urls import path
from django.urls import path
from .views import home, menu,about,review,items,cart,login


urlpatterns = [
    path('home',home,name='home'),
    path('menu',menu,name='menu'),
    path('menu/<str:name>',items,name='items'),
    path('cart',cart,name='cart'),
    path('login',login,name='login'),
    path('about',about,name='about'),
    path('review',review,name='review')
]
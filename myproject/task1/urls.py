from django.urls import path
from .views import platform, games, cart, register

urlpatterns = [
    path('', platform, name='platform'),
    path('games/', games, name='games'),
    path('cart/', cart, name='cart'),
    path('register/', register, name='register'),
]
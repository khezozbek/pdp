from django.urls import path
from .views import menu_views

urlpatterns = [
    path('', menu_views, name='menu-o'),
]

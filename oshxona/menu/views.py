from django.shortcuts import render
from .models import Menu


def menu_views(request):
    menu = Menu.objects.all()
    return render(request, 'menu/index.html', {
        'menu': menu
    })

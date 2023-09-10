from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class menu_admin(admin.ModelAdmin):
    list_display = ('title', 'img', 'text')
    search_fields = ('title', )

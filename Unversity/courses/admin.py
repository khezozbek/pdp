from django.contrib import admin
from .models import User,Book,Bookrecord,Teacher

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Bookrecord)
admin.site.register(Teacher)

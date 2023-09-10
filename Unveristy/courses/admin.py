from django.contrib import admin

from .models import Speciality, Teacher, Subject


@admin.register(Speciality)
class SpecialtyAdmin(admin.ModelAdmin):
    search_fields = ("name", 'code')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ("frist_name", "last_name")
    list_display = ("frist_name", "degree")
    list_filter = ("frist_name", )



@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    list_display = ("name",)
    autocomplete_fields = ("specialities", "teachers", )

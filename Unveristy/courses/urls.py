from django.urls import path
from .views import (
    spec_create, spec_list, spec_detail, sub_lis, sub_detail, teacher_create, teach_list, subject_create, teach_detail
                    )

urlpatterns = [
    path('main/', spec_list, name='spec-list'),
    path('main/<int:pk>', spec_detail, name='spec-detail'),
    path('courses/subject/', sub_lis, name='sub-list'),
    path('courses/subject/<int:pk>', sub_detail, name='sub-detail'),
    path('courses/speciality/create', spec_create, name='spec-create'),
    path('courses/teacher/create', teacher_create, name='teach-create'),
    path('courses/teacher/', teach_list, name='teach-list'),
    path('courses/subject/create', subject_create, name='sub-create'),
    path('courses/teacher/<int:pk>', teach_detail, name='teach-detail'),
]

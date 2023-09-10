from django.urls import path
from .views import teach_list, teach_detail
urlpatterns = [
    path('courses/teacher/', teach_list, name='teach-list'),
    path('courses/teacher/<int:pk>/', teach_detail, name="teach-detail")

]
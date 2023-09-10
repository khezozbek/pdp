from django.urls import path, include
from .views import ActorAPIView, MovieAPIView, MovieViewSet, ActorViewSet
from rest_framework.routers import DefaultRouter
from .views import CommentApiView, CommentDeleteApiViews
router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actor', ActorViewSet)

urlpatterns = [
    path('rot', include(router.urls)),
    path('actor_list/', ActorAPIView.as_view(), name='actor'),
    path('movi_list/', MovieAPIView.as_view(), name='movie'),
    path('comment_1/', CommentApiView.as_view(), name='coment-1'),
    path('comment_delete/<int:pk>', CommentDeleteApiViews.as_view(), name='coment-delete'),
    path('comment_list', CommentApiView.as_view(), name='comment_list')

]


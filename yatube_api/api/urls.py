from rest_framework import routers

from django.urls import include, path

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet, basename='post')
router_v1.register('groups', GroupViewSet, basename='group')
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments'),
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('djoser.urls')),  # Работа с пользователями
    path('v1/', include('djoser.urls.jwt')),  # Работа с токенами
]

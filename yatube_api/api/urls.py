from api.views import (CommentViewSet, GroupViewSet, PostViewSet,
                       FollowViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register(r'posts/(?P<post_id>[^/W]+)/comments',
                   CommentViewSet, basename='comments')
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]

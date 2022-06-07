from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from api.serializers import FollowSerializer
from posts.models import User


class FollowMixin(mixins.ListModelMixin, mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    pass


class FollowViewSet(FollowMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

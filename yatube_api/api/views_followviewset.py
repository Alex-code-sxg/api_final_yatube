from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, mixins
# from rest_framework import status
# from rest_framework.response import Response
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
# class FollowViewSet(viewsets.ViewSet):
#    permission_classes = (IsAuthenticated,)
#    filter_backends = (filters.SearchFilter,)
#    search_fields = ('following__username', 'user__username')
#
#    def list(self, request):
#        user = get_object_or_404(User, username=self.request.user.username)
#        queryset = user.follower
#        serializer = FollowSerializer(queryset, many=True)
#        return Response(serializer.data)
#
#    def create(self, request):
#        serializer = FollowSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save(user=self.request.user)
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

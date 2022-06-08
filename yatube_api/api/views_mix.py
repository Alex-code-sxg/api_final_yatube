from rest_framework import viewsets, mixins


class FollowMixin(mixins.ListModelMixin, mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    pass

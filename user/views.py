from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet

from user.models import User, Post, PostLike
from user.serializers import (
    UserListSerializer,
    UserDetailSerializer,
    PostSerializer,
    PostLikeSerializer,
)


class UserViewSet(
    viewsets.ModelViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(username=self.request.user)
        if self.action == "list":
            return self.queryset.all()
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer

        return UserDetailSerializer


class PostViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostLikeViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

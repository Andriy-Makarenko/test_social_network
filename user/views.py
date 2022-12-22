from rest_framework import mixins, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.viewsets import GenericViewSet

from user.models import User, Post, PostLike
from user.serializers import (
    UserListSerializer,
    UserListPutSerializer,
    UserDetailSerializer,
    PostSerializer,
    PostListSerializer,
    PostDetailSerializer,
    PostLikeSerializer,
)


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset.filter(username=self.request.user)
        if self.action == "list":
            return self.queryset.all()

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        if self.action in ["update", "partial_update"]:
            return UserListPutSerializer
        if self.action == "create":
            return UserDetailSerializer

        return UserDetailSerializer


class PostViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        if self.action == "list":
            return self.queryset.all()  # shows all users posts

        return queryset

    def perform_create(self, serializer):  # Set current user as post author
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        if self.action == "retrieve":
            return PostDetailSerializer

        return PostSerializer


class PostLikeViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = (IsAuthenticated,)


class CreateTokenView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

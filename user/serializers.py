from rest_framework import serializers
from .models import User, Post, PostLike


class PostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "post", "user", "like_count", "unlike_count", "creation_date")


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "post", "user", "like_count")


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "post", "like_count", "unlike_count", "creation_date", "likes")
        extra_kwargs = {"likes": {"write_only": True}}


class UserListSerializer(serializers.ModelSerializer):
    posts = PostListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "posts")
        read_only_fields = ("last_login", "date_joined")


class UserListPutSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class UserDetailSerializer(serializers.ModelSerializer):
    posts = PostDetailSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "password",
            "username",
            "first_name",
            "last_name",
            "is_staff",
            "email",
            "last_login",
            "date_joined",
            "posts"
        )
        read_only_fields = (
            "first_name",
            "last_name",
            "is_staff",
            "email",
            "last_login",
            "date_joined"
        )
        extra_kwargs = {"password": {"write_only": True}}


class PostLikeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    post_like = serializers.CharField(source="post_like.post", read_only=True)

    class Meta:
        model = PostLike
        fields = ("id", "like", "user", "post_like")

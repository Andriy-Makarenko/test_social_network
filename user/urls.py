from django.urls import path, include
from rest_framework import routers

from user.views import (
    UserViewSet,
    PostViewSet,
    PostLikeViewSet,
)


router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("posts", PostViewSet)
router.register("likes", PostLikeViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "user"

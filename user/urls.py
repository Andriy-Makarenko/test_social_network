from django.urls import path, include
from rest_framework import routers

from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from user.views import (
    UserViewSet,
    PostViewSet,
    PostLikeViewSet,
    CreateTokenView,
    ManageUserView,
)


router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("posts", PostViewSet)
router.register("likes", PostLikeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

app_name = "user"

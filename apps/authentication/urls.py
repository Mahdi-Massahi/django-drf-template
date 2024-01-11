from rest_framework import routers
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserViewSet, CurrentUserView

router = routers.DefaultRouter()

router.register(r"user", UserViewSet)


urlpatterns = [
    path("current_user/", CurrentUserView.as_view(), name="current_user"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]

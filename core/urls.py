from django.contrib import admin
from django.urls import path, include

from apps.authentication.urls import router as auth_router
from .swagger.urls import urlpatterns as swagger_router


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include(auth_router.urls)),
    path("api/", include(swagger_router)),
]

from django.contrib import admin
from django.urls import path, include

from apps.authentication.urls import urlpatterns as auth_urlpatterns
from .swagger.urls import urlpatterns as swagger_router


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include(auth_urlpatterns)),
    path("", include(swagger_router)),
]

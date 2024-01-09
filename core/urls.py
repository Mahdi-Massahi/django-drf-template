from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

from apps.authentication.urls import urlpatterns as auth_urlpatterns
from .swagger.urls import urlpatterns as swagger_router


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include(auth_urlpatterns)),
    # Swagger
    path("api/", include(swagger_router)),
    re_path(
        route=r"^static/(?P<path>.*)$",
        view=serve,
        kwargs={
            "document_root": settings.STATIC_ROOT,
        },
    ),
]

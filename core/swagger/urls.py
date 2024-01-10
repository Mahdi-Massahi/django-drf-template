from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from .views import schema_view


urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    re_path(
        route=r"^static/(?P<path>.*)$",
        view=serve,
        kwargs={
            "document_root": settings.STATIC_ROOT,
        },
    ),
]

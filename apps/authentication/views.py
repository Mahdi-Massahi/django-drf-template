from rest_framework import viewsets, mixins

from .models import User
from .serializers import UserSerializer


class UserViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

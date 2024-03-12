from rest_framework.generics import CreateAPIView

from apps.blog.api_enpoints.User.UserCreate.serializers import UserCreateSerializer
from apps.blog.models import User


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


__all__ = ('UserCreateView',)

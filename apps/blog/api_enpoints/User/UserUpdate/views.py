from rest_framework.generics import UpdateAPIView

from apps.blog.api_enpoints.User.UserUpdate.serializers import UserUpdateSerializer
from apps.blog.models import User


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


__all__ = ('UserUpdateView',)

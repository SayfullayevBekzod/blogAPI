from rest_framework.generics import UpdateAPIView

from apps.blog.api_enpoints.User.UserUpdatePassword.serializers import UserUpdatePasswordSerializer
from apps.blog.models import User


class UserUpdatePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdatePasswordSerializer


__all__ = ('UserUpdatePasswordView',)

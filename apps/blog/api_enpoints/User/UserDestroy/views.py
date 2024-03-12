from rest_framework.generics import DestroyAPIView

from apps.blog.api_enpoints.User.UserDestroy.serializers import UserDestroySerializer
from apps.blog.models import User


class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer


__all__ = ('UserDestroyView',)

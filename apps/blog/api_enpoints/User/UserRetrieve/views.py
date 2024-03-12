from rest_framework.generics import RetrieveAPIView

from apps.blog.api_enpoints.User.UserRetrieve.serializers import UserRetrieveSerializer
from apps.blog.models import User


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer


__all__ = ('UserRetrieveView',)

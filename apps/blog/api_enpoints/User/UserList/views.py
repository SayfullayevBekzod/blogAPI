from rest_framework.generics import ListAPIView

from apps.blog.api_enpoints.User.UserList.serialziers import UserListSerializer
from apps.blog.models import User


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


__all__ = ('UserListView',)

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView

from apps.blog.api_enpoints.User.UserList.serialziers import UserListSerializer
from apps.blog.dedugger import debugger
from apps.blog.models import User


class UserListView(ListAPIView):
    queryset = User.objects.all().prefetch_related('posts', 'comments')
    serializer_class = UserListSerializer

    @method_decorator(cache_page(60 * 10))
    @debugger
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


__all__ = ('UserListView',)

from rest_framework.generics import DestroyAPIView

from apps.blog.api_enpoints.User.UserDestroy.serializers import UserDestroySerializer
from apps.blog.models import Post


class PostDestroyView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = UserDestroySerializer


__all__ = ('PostDestroyView',)

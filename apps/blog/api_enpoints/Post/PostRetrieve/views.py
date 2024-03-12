from rest_framework.generics import RetrieveAPIView

from apps.blog.api_enpoints.User.UserRetrieve.serializers import UserRetrieveSerializer
from apps.blog.models import Post


class PostRetrieveView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = UserRetrieveSerializer


__all__ = ('PostRetrieveView',)

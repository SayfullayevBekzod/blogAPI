from rest_framework.generics import UpdateAPIView

from apps.blog.api_enpoints.Post.PostUpdate.serializers import PostUpdateSerializer
from apps.blog.models import Post


class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer


__all__ = ('PostUpdateView',)

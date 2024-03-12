from rest_framework.generics import  ListAPIView

from apps.blog.api_enpoints.Post.PostList.serializers import PostListSerializer
from apps.blog.models import Post


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


__all__ = ('PostListView',)

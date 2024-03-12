from rest_framework.generics import CreateAPIView

from apps.blog.api_enpoints.Post.PostCreate.serializers import PostCreateSerializer
from apps.blog.models import Post


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


__all__ = ('PostCreateView',)

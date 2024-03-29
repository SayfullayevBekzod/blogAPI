from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView

from apps.blog.api_enpoints.Post.PostList.serializers import PostListSerializer
from apps.blog.dedugger import debugger
from apps.blog.models import Post


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    @method_decorator(cache_page(60 * 15))
    @debugger
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


__all__ = ('PostListView',)

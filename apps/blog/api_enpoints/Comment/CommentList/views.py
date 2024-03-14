from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView

from apps.blog.dedugger import debugger
from apps.blog.models import Comment
from apps.blog.serializers import CommentListSerializer


class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

    @method_decorator(cache_page(60 * 10))
    @debugger
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


__all__ = ('CommentListView',)

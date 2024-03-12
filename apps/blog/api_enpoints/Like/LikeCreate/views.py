from rest_framework.generics import CreateAPIView

from apps.blog.api_enpoints.Like.LikeCreate.serializers import LikeCreateSerializer
from apps.blog.models import Like


class LikeCreateView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeCreateSerializer


__all__ = ('LikeCreateView',)

from rest_framework.generics import UpdateAPIView

from apps.blog.api_enpoints.Like.LikeUpdate.serializers import LikeUpdateSerializer
from apps.blog.models import Like


class LikeUpdateView(UpdateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeUpdateSerializer


__all__ = ('LikeUpdateView',)

from rest_framework.generics import DestroyAPIView

from apps.blog.api_enpoints.Like.LikeDestroy.serializers import LikeDestroySerializer
from apps.blog.models import Like


class LikeDestroyView(DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeDestroySerializer


__all__ = ('LikeDestroyView', )

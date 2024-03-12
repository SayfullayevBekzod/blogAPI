from rest_framework.generics import RetrieveAPIView

from apps.blog.api_enpoints.Like.LikeRetrieve.serializers import LikeRetrieveSerializer
from apps.blog.models import Like


class LikeRetrieveView(RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeRetrieveSerializer


__all__ = ('LikeRetrieveView',)

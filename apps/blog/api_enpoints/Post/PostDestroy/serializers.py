from rest_framework.serializers import ModelSerializer

from apps.blog.models import Post


class PostDestroySerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body', 'is_active', 'user_id')
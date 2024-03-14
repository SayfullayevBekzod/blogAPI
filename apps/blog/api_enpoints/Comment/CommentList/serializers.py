from rest_framework.serializers import ModelSerializer

from apps.blog.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body', 'post_id', 'user_id')

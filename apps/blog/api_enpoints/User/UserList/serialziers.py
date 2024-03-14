from rest_framework.serializers import ModelSerializer

from apps.blog.models import User


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'bio')

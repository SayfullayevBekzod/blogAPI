from rest_framework.serializers import ModelSerializer

from apps.blog.models import User


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'birthday', 'bio')

from rest_framework.serializers import ModelSerializer

from apps.blog.models import User


class UserUpdatePasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('password', )

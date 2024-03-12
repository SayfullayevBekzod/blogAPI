from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, ListSerializer

from apps.blog.models import User, Post, Comment, Like


class UserCreateSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'bio', 'password')

    def validate_username(self, value):
        if not value.isalpha():
            raise ValidationError('Username must contains only letters')
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        username = validated_data.pop('username')
        bio = validated_data.pop('bio')
        user = User(username=username, bio=bio, password=password)
        user.set_password(password)
        user.save()
        return user


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'bio', 'password')


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'is_active', 'user_id', 'like_count')


class CommentListSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'body', 'post_id', 'user_id', 'like_count')


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body', 'user_id', 'post_id', 'like_count')

        def create(self, validated_data):
            body = validated_data.pop('body')
            post_id = validated_data.pop('post_id')
            user_id = validated_data.pop('user_id')
            like_count = validated_data.pop('like_count')
            comment = Comment(body=body, post_id=post_id, user_id=user_id, like_count=like_count)
            comment.save()
            return comment


class CommentLikeListSerializer(ModelSerializer):
    # likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('body', 'post_id', 'user_id')


class PostDetailSerializer(ModelSerializer):
    comments = CommentListSerializer(many=True, read_only=True)

    # likes = LikeSerializer(many=True)

    class Meta:
        model = Post
        fields = ('title', 'body', 'is_active', 'user_id', 'comments', 'likes')


class MiniUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class MiniPostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title')


class LikeSerializer(ModelSerializer):
    user_id = MiniUserSerializer()
    post_id = MiniPostSerializer()

    class Meta:
        model = Like
        fields = ('user_id', 'post_id')

        def create(self, validated_data):
            post_id = validated_data.pop('post_id')
            user_id = validated_data.pop('user_id')
            created_at = validated_data.pop('created_at')
            like = Like(post_id=post_id, user_id=user_id, created_at=created_at)
            like.save()
            return like

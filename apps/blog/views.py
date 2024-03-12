from django.db.models import Q, Count
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action
from apps.blog.models import User, Post, Comment, Like
from apps.blog.serializers import UserCreateSerializer, UserListSerializer, PostSerializer, \
    CommentCreateSerializer, CommentLikeListSerializer, PostDetailSerializer, LikeSerializer, CommentListSerializer


class UserViewSet(ViewSet):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'detail': 'User registered'}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={'detail': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # permission_classes = [IsOwner, ]

    # permission_classes = [IsAuthenticated, ]

    @action(detail=True, methods=['POST'], url_path='pres_like')
    def like_post(self, *args, **kwargs):
        post = self.get_object()
        user = self.request.user
        like = Like.objects.create(post_id=post, user_id=user)
        serializer = LikeSerializer(like)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['PUT'], url_path='dislike')
    def dislike_post(self, *args, **kwargs):
        post = self.get_object()
        user = self.request.user
        like = get_object_or_404(Like, post_id=post, user_id=user)
        like.delete()
        return Response(status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def retrieve(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        serializer = PostDetailSerializer(post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], url_path='top_posts')
    def top_posts(self, request, *args, **kwargs):
        top_posts = Post.objects.annotate(like_count=Count('like_count ')).order_by('-like_count')[:3]
        serializer = PostSerializer(top_posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['post_likes', 'id', '-id']
    search_fields = ['body', 'post_id', 'user_id']


def get_queryset(self):
    search = self.request.query_params = ['search']
    queryset = Comment.objects.all()
    queryset = queryset.filter(
        Q(body__icontains=search) & Q(post_id__title__icontains=search) & Q(user_id__username__icontains=search))
    return queryset


def post(self, request):
    serializer = CommentCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={'detail': 'Comment added'}, status=status.HTTP_201_CREATED)
    else:
        return Response(data={'detail': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)


def list(self, request):
    queryset = Comment.objects.all().select_related('user_id', 'post_id')
    serializer = CommentListSerializer(queryset, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


def retrieve(self, request, pk, *args, **kwargs):
    comment = get_object_or_404(Comment, pk=pk)
    serializer = CommentLikeListSerializer(comment)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@action(detail=True, methods=['POST'], url_path='like')
def like_comment(self, *args, **kwargs):
    comment = self.get_object()
    user_id = self.request.user
    like = Comment.objects.create(post_id=comment, user_id=user_id)
    serializer = LikeSerializer(like)
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)

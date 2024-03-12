from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from apps.blog.api_enpoints.Like import LikeListView, LikeCreateView, LikeRetrieveView, LikeUpdateView, LikeDestroyView
from apps.blog.api_enpoints.Post import PostListView, PostCreateView, PostRetrieveView, PostUpdateView, PostDestroyView
from apps.blog.api_enpoints.User import UserDestroyView, UserUpdateView, UserRetrieveView, UserUpdatePasswordView
from apps.blog.api_enpoints.User.UserCreate import UserCreateView
from apps.blog.api_enpoints.User.UserList.views import UserListView
from apps.blog.views import UserViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
#
# router.register('users', UserViewSet, 'user')
# router.register('posts', PostViewSet, 'posts')
# router.register('comment', CommentViewSet, 'comment')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.obtain_auth_token),
    path('like/', LikeListView.as_view()),
    path('like/create', LikeCreateView.as_view()),
    path('like/<pk>/retrieve/', LikeRetrieveView.as_view()),
    path('like/<pk>/update/', LikeUpdateView.as_view()),
    path('like/<pk>/destroy/', LikeDestroyView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/create', UserCreateView.as_view()),
    path('users/<pk>/destroy/', UserDestroyView.as_view()),
    path('users/<pk>/update/', UserUpdateView.as_view()),
    path('users/<pk>/retrieve/', UserRetrieveView.as_view()),
    path('users/<pk>/update/password/', UserUpdatePasswordView.as_view()),
    path('post/', PostListView.as_view()),
    path('post/create', PostCreateView.as_view()),
    path('post/<pk>/destroy/', PostDestroyView.as_view()),
    path('post/<pk>/update/', PostUpdateView.as_view()),
    path('post/<pk>/retrieve/', PostRetrieveView.as_view()),

]
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from posts.models import Group, Post
from .mixins import CreateListViewSet
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)


User = get_user_model()


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    ]
    pagination_class = LimitOffsetPagination
    filterset_fields = ('group', 'author')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    ]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('=user__username', '=following__username')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, mixins

from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group
from .serializers import PostSerializer, CommentSerializer
from .serializers import GroupSerializer, FollowSerializer
from .permissions import AuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author')
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        new_queryset = post.comments.select_related('post', 'author')
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        new_queryset = user.follower.select_related('following')
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

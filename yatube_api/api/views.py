from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import permissions

from api.serializers import CommentSerializer
from api.serializers import FollowSerializer
from api.serializers import GroupSerializer
from api.permissions import OwnerOrReadOnly
from api.serializers import PostSerializer

from posts.models import Post, Group, User


class PostViewSet(viewsets.ModelViewSet):
    """A viewset for viewing and editing posts"""

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = LimitOffsetPagination
    permission_classes = [OwnerOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewList(viewsets.ReadOnlyModelViewSet):
    """A viewset for viewing groups"""

    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class CommentViewList(viewsets.ModelViewSet):
    """A viewset for viewing and editing comments"""

    serializer_class = CommentSerializer
    permission_classes = [OwnerOrReadOnly, ]

    def get_comment_post(self):
        return get_object_or_404(Post,
                                 id=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_comment_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        post=self.get_comment_post())


class FollowViewList(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """A viewset for viewing and creating user-following pairs"""

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    permission_classes = [permissions.IsAuthenticated, ]
    search_fields = ('following__username',)

    def get_queryset(self):
        return get_object_or_404(User, id=self.request.user.id).following.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


from rest_framework import mixins
from rest_framework import viewsets
from postapp.models import Post
from postapp.serializers import PostSerializer

class PostViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset


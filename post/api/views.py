from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import RetrieveDestroyAPIView,DestroyAPIView,UpdateAPIView
from post.api.serializers import CategorySerializer
from post.api.serializers import PostSerializer
from post.models import Categories
from post.models import Post
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from post.permissions import IsOwner



class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title","content"]



    def get_queryset(self):
        queryset = Post.objects.filter(draft = False)
        return queryset

class PostDetailAPIView(RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "href"



class PostDeleteAPIView(DestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "href"
    permission_classes = [IsAdminUser,IsOwner]


class PostUpdateAPIView(UpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "href"
    permission_classes = [IsAdminUser,IsOwner]


class PostCreateAPIView(CreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser,IsOwner]




class CategoryListAPIView(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer



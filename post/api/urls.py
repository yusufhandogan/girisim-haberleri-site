from django.urls import path
from post.api.views import CategoryListAPIView
from post.api.views import PostCreateAPIView
from post.api.views import PostDeleteAPIView
from post.api.views import PostDetailAPIView
from post.api.views import PostListAPIView,PostUpdateAPIView

app_name = "post"

urlpatterns = [
    path("list", PostListAPIView.as_view(), name="list"),
    path("detail/<href>", PostDetailAPIView.as_view(), name="detail"),
    path("category", CategoryListAPIView.as_view(), name="category"),
    path("delete/<href>", PostDeleteAPIView.as_view(), name="delete"),
    path("update/<href>", PostUpdateAPIView.as_view(), name="update"),
    path("create", PostCreateAPIView.as_view(), name="create"),
    path("detail/<href>", PostDetailAPIView.as_view(), name="detail"),
]

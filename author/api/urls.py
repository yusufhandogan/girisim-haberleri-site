from django.urls import path

from author.api.views import AuthorCreateAPIView, AuthorDeleteAPIView, AuthorDetailAPIView, AuthorListAPIView, AuthorUpdateAPIView


app_name = "author"

urlpatterns = [
    path("list", AuthorListAPIView.as_view(), name="list"),
    path("detail/<href>", AuthorDetailAPIView.as_view(), name="detail"),
    path("delete/<href>", AuthorDeleteAPIView.as_view(), name="delete"),
    path("update/<href>", AuthorUpdateAPIView.as_view(), name="update"),
    path("create", AuthorCreateAPIView.as_view(), name="create"),
]

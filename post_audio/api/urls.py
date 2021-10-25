from django.urls import path
from post_audio.api.views import PostAudioListAPIView, PostAudioDetailAPIView, PostAudioDeleteAPIView, PostAudioUpdateAPIView, PostAudioCreateAPIView


app_name = "postaudio"

urlpatterns = [
    path("list", PostAudioListAPIView.as_view(), name="list"),
    path("detail/<href>", PostAudioDetailAPIView.as_view(), name="detail"),
    path("delete/<href>", PostAudioDeleteAPIView.as_view(), name="delete"),
    path("update/<href>", PostAudioUpdateAPIView.as_view(), name="update"),
    path("create", PostAudioCreateAPIView.as_view(), name="create"),
]

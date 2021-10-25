from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import RetrieveDestroyAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from post_audio.api.serializers import PostAudioSerializer
from post_audio.models import PostAudio


class PostAudioListAPIView(ListAPIView):
    serializer_class = PostAudioSerializer


    def get_queryset(self):
        queryset = PostAudio.objects.filter(draft = False)
        return queryset

class PostAudioDetailAPIView(RetrieveAPIView):

    queryset = PostAudio.objects.all()
    serializer_class = PostAudioSerializer
    lookup_field = "href"

class PostAudioDeleteAPIView(DestroyAPIView):

    queryset = PostAudio.objects.all()
    serializer_class = PostAudioSerializer
    lookup_field = "href"
    permission_classes = [IsAdminUser,]

class PostAudioUpdateAPIView(UpdateAPIView):

    queryset = PostAudio.objects.all()
    serializer_class = PostAudioSerializer
    lookup_field = "href"
    permission_classes = [IsAdminUser,]


class PostAudioCreateAPIView(CreateAPIView):

    queryset = PostAudio.objects.all()
    serializer_class = PostAudioSerializer
    permission_classes = [IsAdminUser,]

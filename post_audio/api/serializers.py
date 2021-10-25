from post_audio.models import PostAudio
from rest_framework import serializers



class PostAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAudio
        fields = [
            "authorId",
            "title",
            "audioUrl",
            "desc",
            "categoriesId",
            "content",
            "href",
            "draft",
            "readingTime",
            "published",
            "featuredimage",
    ]
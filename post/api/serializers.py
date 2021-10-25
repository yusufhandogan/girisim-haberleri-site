from rest_framework import serializers
from post.models import Categories
from post.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "id",
            "authorId",
            "title",
            "content",
            "desc",
            "categoryID",
            "content",
            "href",
            "readingtime",
            "updated",
            "date",
            "published",
            "featuredimage",
            "draft",
            "postType"
        ]



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = [
            "name",
            "color",
            "href",
            "thumbnail",
    ]



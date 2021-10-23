from rest_framework import serializers
from post.models import Categories
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    href = serializers.HyperlinkedIdentityField(
        view_name="post:detail",
        lookup_field= "href",
    )
    class Meta:
        model = Post
        fields = [
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



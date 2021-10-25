from author.models import Account
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from comment.models import CommentModel
from post.models import Post


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = CommentModel
        exclude = ['date',]

    def validate(self, attrs):
        if(attrs["parent"]):
            if attrs["parent"].post != attrs["post"]:
                raise serializers.ValidationError("something went wrong")
        return attrs


class UserSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('firstName','lastName','id','email')


class PostCommentSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','href','id')

class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = UserSerializer()
    post = PostCommentSerializer()
    class Meta:
        model = CommentModel
        fields = '__all__'

    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data

class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = [ 
            'content'
        ]
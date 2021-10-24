from rest_framework import serializers
from author.models import Account

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "firstName",
            "lastName",
            "displayName",
            "avatar",
            "bgImage",
            "slug",
            "desc",
            "jobName",
    ]

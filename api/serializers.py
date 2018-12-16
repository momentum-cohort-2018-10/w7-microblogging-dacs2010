from core.models import Post, User
from rest_framework import serializers


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class PostSerializer(serializers.ModelSerializer):
    # posted_by = UserSerializer(many=True, read_only=True)
    user = UserSerialzer(many=True, read_only=True, required=False)

    class Meta:
        model = Post
        lookup_field = 'pk'
        fields = ('user', 'date_created', 'body',)

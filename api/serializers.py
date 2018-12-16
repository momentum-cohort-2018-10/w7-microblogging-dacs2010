from core.models import Post, User
from rest_framework import serializers


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class PostSerializer(serializers.ModelSerializer):
    # posted_by = serializers.StringRelatedField(many=True)
    # user = UserSerialzer(many=True, read_only=True, required=False)
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        lookup_field = 'pk'
        fields = ('user', 'date_created', 'body',)

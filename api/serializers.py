from rest_framework import serializers
from core.models import Post, User, Comment


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class PostSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        lookup_field = 'pk'
        fields = ('user', 'date_created', 'title', 'body',)


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    post = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Comment
        fields = ('user', 'body', 'post')

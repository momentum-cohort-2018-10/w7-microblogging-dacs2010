from core.models import Post, User
from rest_framework import serializers


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        lookup_field = 'pk'
        user = UserSerialzer(many=True)
        fields = ('user', 'date_created', 'body')

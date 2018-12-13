from core.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        lookup_field = 'pk'
        fields = ('user', 'title', 'date_created', 'body')

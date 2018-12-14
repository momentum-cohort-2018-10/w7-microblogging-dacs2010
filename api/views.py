from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from core.models import Post
from api.serializers import PostSerializer

# Create your views here.
@api_view(['GET'])
def post_list(request):
    '''
    a list o f all the posts
    '''
    if request.method == 'GET':
        posts = Post.objects.all()
        lookup_field = 'pk'
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)
        

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.request.user.posts

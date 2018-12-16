from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from core.models import Post, User, Comment
from api.serializers import PostSerializer, UserSerialzer, CommentSerializer


# Create your views here.
class CommentsListView(generics.ListAPIView):
    '''
    comments list
    '''
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


@api_view(['GET'])
def post_list(request):
    '''
    a list of all the posts
    '''
    if request.method == 'GET':
        posts = Post.objects.all()
        lookup_field = 'pk'
        serializer = PostSerializer(
            posts,
            many=True,
            context={'request': request}
            )
        return Response(serializer.data)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    '''
    individual posts
    '''
    serializer_class = PostSerializer
    lookup_field = 'pk'
    queryset = Post.objects.all()

    # def get_queryset(self):
    #     '''
    #     returns post for authenticated user
    #     '''
    #     return self.request.user.posts


class UserListView(generics.ListAPIView):
    '''
    a list of all the users
    '''
    serializer_class = UserSerialzer
    queryset = User.objects.all()

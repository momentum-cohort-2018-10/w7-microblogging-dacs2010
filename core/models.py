from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class Post(models.Model):
    '''
    Posts
        user
        title
        date_created
        likes
        comments
    '''
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=255)
    likes = 
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE)


class User(AbstractBaseUser):
    '''
    User
        like
        follow
        followed_by
    '''
    pass


class Comment(models.Model):
    '''
        likes
    '''
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)


'''
Like
    user
    post
    comment
'''


'''
Follow
    user_to
    user_from
'''

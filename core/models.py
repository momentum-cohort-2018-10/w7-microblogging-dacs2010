from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
    like
    follow
    followed_by
    '''
    pass


class Post(models.Model):
    '''
    likes
    comments
    '''
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=255)





# class Comment(models.Model):
#     '''
#         likes
#     '''
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     body = models.CharField(max_length=255)
#     post = models.ForeignKey(to=Post, on_delete=models.CASCADE)


# '''
# Like
#     user
#     post
#     comment
# '''


# class Follow(models.Model):
# '''
# Follow
#     following
#     leading
# '''
# pass

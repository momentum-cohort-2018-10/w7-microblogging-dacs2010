from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
    like
    '''
    followed_users = models.ManyToManyField(
        to='User',
        through='Follow',
        through_fields=('follower', 'followee'),
        related_name="followers",
     )


class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=255)


class Follow(models.Model):
    follower = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='followed_by')

    followee = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='following')

    date_created = models.DateTimeField(auto_now_add=True)


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



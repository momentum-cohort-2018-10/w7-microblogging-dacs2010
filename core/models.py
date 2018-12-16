from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
    to do:
    like
    '''
    followed_users = models.ManyToManyField(
        to='User',
        through='Follow',
        through_fields=('follower', 'followee'),
        related_name="followers",
    )

    def __str__(self):
        return self.username


class Post(models.Model):
    '''
    to do:
        likes
    '''
    user = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        related_name='posted_by'
    )
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=280)

    def __str__(self):
        return self.title


class Follow(models.Model):
    follower = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        related_name='followed_by'
    )
    followee = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='following'
    )
    date_created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    '''
    to do:
        likes
    '''
    user = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE, 
        related_name='commented_by')
    body = models.CharField(max_length=255)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)


# '''
# Like
#     user
#     post
#     comment
# '''



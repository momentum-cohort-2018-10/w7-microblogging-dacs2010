from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import Post, User, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    model = Post
    fields = ('body', 'user')

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    fields = ('user', 'body', 'post')


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
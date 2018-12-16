from django.contrib import admin
from core.models import Post, User, Comment
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    '''
    user admin
    '''
    fields = ('username', 'email', 'is_active')
    search_fields = ('user',)


class CommentAdmin(admin.ModelAdmin):
    '''
    comment admin
    '''
    model = Comment
    fields = ('user', 'body', 'post')
    extra = 1


class PostAdmin(admin.ModelAdmin):
    '''
    post admin
    '''
    model = Post
    list_display = ['title', 'body', 'user']


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

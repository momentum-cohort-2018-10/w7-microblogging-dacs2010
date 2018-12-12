from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import Post, User
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    model = Post
    fields =('body', 'user')


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
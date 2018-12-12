from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    data = ('body', '')
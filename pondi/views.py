from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Post, Prompt, Profile
from .serializers import PostCreateSerializer

from pondi.models import Profile, Post, Prompt

userName = 1 #use api given userName
userPosts = Post.objects.filter(profile__user__username = userName)

#TODO: Convert userPosts to json and send to front end

Post.objects.filter(profile__closefriends__user__username = username)

Post.objects.filter(profile__friends__user__username = username)


# Create your views here.

# Create your views here.

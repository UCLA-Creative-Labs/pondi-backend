from django.shortcuts import render

from pondi.models import Profile, Post, Prompt

userName = 1 #use api given userName
userPosts = Post.objects.filter(profile__user__username = userName)

#TODO: Convert userPosts to json and send to front end

Post.objects.filter(profile__closefriends__user__username = username)

Post.objects.filter(profile__friends__user__username = username)


# Create your views here.

# Create your views here.

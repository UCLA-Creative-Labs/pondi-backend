from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Post, Prompt, Profile


from pondi.models import Profile, Post, Prompt, User
from rest_framework.decorators import api_view
from pondi.serializers import ProfileSerializer
from rest_framework.response import Response
import json

userName = 1 #use api given userName
userPosts = Post.objects.filter(profile__user__username = userName)

#TODO: Convert userPosts to json and send to front end

#Post.objects.filter(profile__closefriends__user__username = username)

#Post.objects.filter(profile__friends__user__username = username)


# Create your views here.
@api_view(['GET', 'POST'])
def send_request(request):
    #Accept a friend when passed in username
    if request.method == 'POST':
        serializer = ProfileSerializer
        myDict = json.loads(request.body)
        friendname = myDict["friendname"]
        acceptor = Profile.objects.get(user__username = friendname)
        acceptor.pendingfriends.add()
        if serializer.is_valid():
           serializer.save()
        return Response(serializer.data)


# Create your views here.



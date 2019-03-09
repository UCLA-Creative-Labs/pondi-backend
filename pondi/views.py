from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Post, Prompt, Profile

from rest_framework.views import APIView
from pondi.models import Profile, Post, Prompt, User
from rest_framework.decorators import api_view
from pondi.serializers import ProfileSerializer, PostSerializer
from rest_framework.response import Response
import json

userName = 1 #use api given userName
userPosts = Post.objects.filter(profile__user__username = userName)



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

class PostView(APIView):
        def put(self, request, pk):
                saved_article = get_object_or_404(Post.objects.all(), pk=pk)
                data = request.data.get('body')
                serializer = PostSerializer(instance=saved_article, data=data, partial=True)
                if serializer.is_valid(raise_exception=True):
                        post_saved = serializer.save()
                return Response({"success": "Post '{}' updated successfully".format(post_saved.prompt)})
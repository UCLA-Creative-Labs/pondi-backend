from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .serializers import (CreateUserSerializer, ProfileSerializer, UserSerializer, LoginUserSerializer, PostSerializer, AcceptFriendSerializer)
from .models import Post, Profile, User
from rest_framework.views import APIView

from knox.models import AuthToken


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": ProfileSerializer(self.request.user.profile, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": ProfileSerializer(self.request.user.profile, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class ProfileAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile



#The API is pretty staight-forward, we validate the user input and create an account if the validation passes. In the response, we return the user object in serialized format and an authentication token which will be used by the application to perform user-specific api calls.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = PostSerializer


    def get_queryset(self):
        return Post.objects.filter(profile__user__username = self.request.user.username)

    def perform_create(self, serializer):
        serializer.save(profile =self.request.profile)

class FriendPostsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = PostSerializer


    def get_queryset(self):
        return (Post.objects.filter(profile__closefriends__user__username = self.request.user.username)
        | Post.objects.filter(profile__friends__user__username = self.request.user.username).exclude(privacy = 'c'))

    def perform_create(self, serializer):
        serializer.save(profile =self.request.profile)

class UpdateProfileAPI(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile
'''
class AcceptFriendRequest(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        myDict = dict(request.data) #request.data is a queryDict --> dict
        tempList = myDict.get("pendingfriends", "nope") #from myDict get List value from myDict
        tempFriend = tempList[0] #get first value which is the added friend
        tempID = Profile.objects.filter(profile_user_username=tempFriend)
        instance.friends.add(tempID)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

'''
class AcceptFriend(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = AcceptFriendSerializer

    def get_object(self):
        return self.request.user.profile

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        tempList=request.data
        tempID=tempList.get("pendingfriends")
        instance.friends.add(tempID)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class AcceptFriendRequest(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProfileSerializer
    def get_object(self):
        return self.request.user.profile
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        #tempFriend = request.GET.get("blue", 'poop')
        myDict = dict(request.data) #request.data is a queryDict --> dict
        tempList = myDict.get("pendingfriends", "nope") #from myDict get List value from myDict
        tempFriend = tempList[0] #get first value which is the added friend
        instance.friends.add(tempFriend)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)





from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Post, Profile, Prompt

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        validated_data['email'],
                                        validated_data['password'])
        return user

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','first_name', 'last_name', 'email')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'animal', 'color', 'friends', 'closefriends', 'pendingfriends')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('prompt', 'body', 'timestamp', 'profile', 'theme')

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

class MyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','prompt', 'body', 'timestamp', 'profile', 'theme', 'privacy')


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ('__all__')

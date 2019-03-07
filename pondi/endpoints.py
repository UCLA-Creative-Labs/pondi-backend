from django.conf.urls import include, url
from rest_framework import routers

from .api import RegistrationAPI, LoginAPI, UserAPI, ProfileAPI, UpdateProfileAPI, AcceptFriendRequest, AcceptFriend, PromptViewSet


router = routers.DefaultRouter()
#router.register('pondi', PostViewSet, 'pondi')

router.register('prompts', PromptViewSet)

urlpatterns = [
    url("^", include(router.urls)),
    url("^auth/register/$", RegistrationAPI.as_view()),
    url("^auth/login/$", LoginAPI.as_view()),
    url("^auth/user/$", UserAPI.as_view()),
    url("^auth/profile/$", ProfileAPI.as_view()),
    url("^auth/update/$", UpdateProfileAPI.as_view()),
    url("^auth/acceptrequest/$", AcceptFriendRequest.as_view()),
    url("^auth/accept/$", AcceptFriend.as_view()),
    url("^prompts/$", include(router.urls)),


]

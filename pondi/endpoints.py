from django.conf.urls import include, url
from rest_framework import routers

from .api import RegistrationAPI, LoginAPI, UserAPI, PostViewSet, ProfileAPI, UpdateProfileAPI, AcceptFriendRequest, AcceptCloseFriendRequest, SendFriendRequest, SearchFriend


router = routers.DefaultRouter()
router.register('pondi', PostViewSet, 'pondi')

urlpatterns = [
    url("^", include(router.urls)),
    url("^auth/register/$", RegistrationAPI.as_view()),
    url("^auth/login/$", LoginAPI.as_view()),
    url("^auth/user/$", UserAPI.as_view()),
    url("^auth/profile/$", ProfileAPI.as_view()),
    url("^auth/update/$", UpdateProfileAPI.as_view()),
    url("^auth/acceptrequest/$", AcceptFriendRequest.as_view()),
    url("^auth/acceptrequestclose/$", AcceptCloseFriendRequest.as_view()),
    url("^auth/sendrequest/$", SendFriendRequest.as_view()),
    url("^auth/searchfriend/$", SearchFriend.as_view()),


]

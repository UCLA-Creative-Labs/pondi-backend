from django.conf.urls import include, url
from rest_framework import routers


from .api import (RegistrationAPI, LoginAPI, UserAPI, ProfilePostViewSet, ProfileAPI,
                  UpdateProfileAPI, AcceptFriendRequest, AcceptCloseFriendRequest,
                  SendFriendRequest, SearchFriend, FriendPostsViewSet, OceanPostViewSet, PostUpdate, FriendProfileViewSet)





router = routers.DefaultRouter()
#router.register('pondi', PostViewSet, 'pondi')


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
    url("^auth/friendposts/$", FriendPostsViewSet.as_view({'get' : 'retrieve'})),
    url("^auth/myposts/$", ProfilePostViewSet.as_view({'get': 'retrieve', 'post':'create', 'patch': 'update'})),
    url("^auth/friendprofile/$", FriendProfileViewSet.as_view({'get': 'retrieve'})),
    url("^auth/oceanposts/$", OceanPostViewSet.as_view({'get': 'retrieve'})),
    url("^prompts/$", include(router.urls)),




]

from django.conf.urls import include, url
from rest_framework import routers

from .api import RegistrationAPI, LoginAPI, UserAPI, PostViewSet, ProfileAPI, UpdateProfileAPI


router = routers.DefaultRouter()
router.register('pondi', PostViewSet, 'pondi')

urlpatterns = [
    url("^", include(router.urls)),
    url("^auth/register/$", RegistrationAPI.as_view()),
    url("^auth/login/$", LoginAPI.as_view()),
    url("^auth/user/$", UserAPI.as_view()),
    url("^auth/profile/$", ProfileAPI.as_view()),
    url("^auth/update/$", UpdateProfileAPI.as_view()),


]

from django.conf.urls import include, url
from rest_framework import routers

from .api import RegistrationAPI

router = routers.DefaultRouter()

urlpatterns = [
    url("^", include(router.urls)),
    url("^auth/register/$", RegistrationAPI.as_view())
]

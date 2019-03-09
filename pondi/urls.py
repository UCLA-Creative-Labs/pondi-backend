from django.urls import path

from .views import PostView


app_name = "pondi"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('pondi/<int:pk>', PostView.as_view()),
]
from django.contrib import admin
from .models import Profile, Post, Prompt
# Register your models here.

admin.site.register(Profile)
admin.site.register(Prompt)
admin.site.register(Post)
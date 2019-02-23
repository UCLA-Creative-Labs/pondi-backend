from django.contrib import admin
from .models import Post, Profile, Prompt

admin.register(Post, Profile, Prompt)(admin.ModelAdmin)

# Register your models here.

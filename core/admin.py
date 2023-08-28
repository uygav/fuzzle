from django.contrib import admin
# import for Profile class from models.py
from .models import Profile, Post, LikePost
# Register your models here.
admin.site.register(Profile)  # we want to control(Profile) from admin panel
admin.site.register(Post)
admin.site.register(LikePost)

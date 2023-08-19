from django.contrib import admin
from .models import Profile, Post  # import for Profile class from models.py
# Register your models here.
admin.site.register(Profile)  # we want to control(Profile) from admin panel
admin.site.register(Post)

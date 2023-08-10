from django.contrib import admin
from .models import Profile  # import for Profile class from models.py
# Register your models here.
admin.site.register(Profile)  # we want to control(Profile) from admin panel

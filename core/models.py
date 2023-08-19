from django.db import models
from django.contrib.auth import get_user_model  # idk
import uuid  # universally unique identifier
from datetime import datetime  # represent date and time


User = get_user_model()

# create your models here


class Profile(models.Model):  # this class about database
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(
        upload_to='profile_images', default='blank-profile-picture-640640.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):  # you dont have to create this 'def'
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

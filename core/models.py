from django.db import models
from django.contrib.auth import get_user_model  # idk
# Create your models here.

User = get_user_model()


class Profile(models.Model):  # this class about database
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(
        upload_to='profile_images', default='blank-profile-picture-640640.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):  # you dont have to create this 'def'
        return self.user.username

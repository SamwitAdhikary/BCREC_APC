from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    message = models.TextField()
    dateTime = models.DateTimeField(auto_created=True, default=datetime.now())

    def __str__(self):
        return "Message from: " + self.name


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(blank=True)

    # additional
    protfolio_site = models.URLField(blank=True)
    # install pillow lib, if you want to work with images.
    profile_pic = models.ImageField(upload_to='pofile_pics', blank=True)
    # in

    def __str__(self):
        return self.user.username

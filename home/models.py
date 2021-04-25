from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import F

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    message = models.TextField()
    # dateTime = models.DateTimeField(auto_created=True, default=datetime.now())

    def __str__(self):
        return "Message from: " + self.name


Course_CHOICES = (
    ('bca', 'BCA'),
    ('bba', 'BBA'),
    ('btech-me', 'B.Tech. ME'),
    ('btech-ce', 'B.Tech. CE'),
    ('btech-ei', 'B.Tech. EI'),
    ('btech-ee', 'B.Tech. EE'),
    ('btech-ec', 'B.Tech. EC'),
    ('btech-it', 'B.Tech. IT'),
    ('btech-cs', 'B.Tech. CS'),
    ('mca', 'MCA'),
    ('mba', 'MBA'),
)

Sem_CHOICES = (
    (1, 'first'),
    (2, 'second'),
    (3, 'third'),
    (4, 'fourth'),
    (5, 'fifth'),
    (6, 'six'),
    (7, 'seven'),
    (8, 'eight'),
)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verify = models.BooleanField(default=False)
    autogen_otp = models.IntegerField()
    name = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(
        max_length=20, default="add mobile number")
    college_name = models.CharField(
        max_length=200, default="Dr. B.C. Roy Engineering College - Durgapur")
    state = models.CharField(max_length=50, default="West Bengal")
    # install pillow lib, if you want to work with images.
    profile_pic = models.ImageField(upload_to='pofile_pics', blank=True)
    course = models.CharField(
        max_length=10, choices=Course_CHOICES, default='BCA')
    Semester = models.IntegerField(choices=Sem_CHOICES, default=1)
    bio = models.CharField(max_length=500, default="update your bio.")
    portfolio_site = models.URLField(blank=True, default="")
    upload_cv = models.FileField(upload_to="user_cvs", blank=True)

    def __str__(self):
        return self.user.username


class YoutubeVideos(models.Model):
    desc = models.CharField(max_length=100, default="")
    link = models.URLField(default="")
    title = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="youtube", default="")

    def __str__(self):
        return self.title


class Developers(models.Model):
    desc = models.TextField(default="")
    name = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="developer", default="")
    nick_name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name

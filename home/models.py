from django.db import models
from django.contrib.auth.models import User

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
    ('b.Tech. ME', 'B.Tech. ME'),
    ('b.Tech. CE', 'B.Tech. CE'),
    ('b.Tech. EI', 'B.Tech. EI'),
    ('b.Tech. EE', 'B.Tech. EE'),
    ('b.Tech. EC', 'B.Tech. EC'),
    ('b.Tech. IT', 'B.Tech. IT'),
    ('b.Tech. CS', 'B.Tech. CS'),
    ('mca', 'MCA'),
    ('mba', 'MBA'),
)

Sem_CHOICES = (
    ('first', 1),
    ('second', 2),
    ('third', 3),
    ('fourth', 4),
    ('fifth', 5),
    ('six', 6),
    ('seven', 7),
    ('eight', 8),
)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(blank=True)

    # additional
    protfolio_site = models.URLField(blank=True)
    # install pillow lib, if you want to work with images.
    profile_pic = models.ImageField(upload_to='pofile_pics', blank=True)

    course = models.CharField(
        max_length=10, choices=Course_CHOICES, default='BCA')
    
    Semester = models.CharField(
        max_length=8, choices=Sem_CHOICES, default=1)

    def __str__(self):
        return self.user.username

class YoutubeVideos(models.Model):
    desc = models.CharField(max_length=100, default="")
    link = models.URLField(default="")
    title = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="youtube", default="")

    def __str__(self):
        return self.title

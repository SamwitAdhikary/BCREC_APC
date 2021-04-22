from django.db import models

# Create your models here.

class Courses(models.Model):
    slug = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="courses/images", default="")
    description = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.description

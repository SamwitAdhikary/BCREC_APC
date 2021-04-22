from django.db import models

# Create your models here.

class Course(models.Model):
    slug = models.CharField(max_length=50, default="", primary_key=True)
    title = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="courses/images", default="", blank=True)
    img_url = models.URLField(blank=True, max_length=1000)
    description = models.CharField(max_length=100, default="")
    yearsOfCourse = models.IntegerField(default=3)

    def __str__(self):
        return self.description

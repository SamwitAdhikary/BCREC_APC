from django.db import models

# Create your models here.

class Course(models.Model):
    slug = models.CharField(max_length=50, default="", primary_key=True)
    title = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="courses/images", default="")
    description = models.CharField(max_length=100, default="")
    yearsOfCourse = models.IntegerField(default=3)
    pdfs = models.FileField(upload_to="pdfs", default="")

    def __str__(self):
        return self.description


class Semester(models.Model):
    sem_number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, blank=True)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - BCa"


class Paper(models.Model):
    paper_name = models.CharField(max_length=100)
    paper_code = models.CharField(max_length=100, null=True)
    semester = models.ForeignKey(Semester, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.paper_name

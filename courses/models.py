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


class Paper(models.Model):
    paperslug = models.CharField(max_length=50, default="")
    paper_name = models.CharField(max_length=100)
    paper_code = models.CharField(max_length=100, null=True)
    semester = models.IntegerField()
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.paper_name

class Year(models.Model):
    year = models.IntegerField(default=0)
    paper_name = models.ForeignKey(Paper, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.year} - {self.paper_name}'
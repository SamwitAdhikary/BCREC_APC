from django.contrib import admin
from .models import Course, Semester, Paper
# Register your models here.

admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Paper)

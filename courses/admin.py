from django.contrib import admin
from .models import Course, Paper,Year
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ("js/tinymce.js",)

admin.site.register(Course, PostAdmin)
admin.site.register(Paper)
admin.site.register(Year)

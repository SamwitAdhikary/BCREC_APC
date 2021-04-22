from django import http
from django.shortcuts import render, HttpResponse
from .models import Course

# Create your views here.
def courses(request):
    # return HttpResponse("This is courses page")
    all_courses = Course.objects.all()
    # print(all_courses)
    context = {'allcourses': all_courses}

    return render(request, 'courses/courses.html', context)

def courses_post(request, slug):
    return HttpResponse(f'This is course for {slug}')

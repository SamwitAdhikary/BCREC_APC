from django import http
from django.shortcuts import render, HttpResponse
from .models import Course, Paper

# Create your views here.


def courses(request):
    # return HttpResponse("This is courses page")
    all_courses = Course.objects.all()
    # print(all_courses)
    context = {'allcourses': all_courses}

    return render(request, 'courses/courses.html', context)


def courses_post(request, slug):
    # return HttpResponse(f'This is course for {slug}')
    course = Course.objects.filter(slug=slug).first()
    context = {'course': course, 'sem':course.yearsOfCourse * 2}
    return render(request, 'courses/courses-details.html', context)


def show_papers(request, slug, sem):
    print(slug, sem)
    papers = Paper.objects.filter(course=slug, semester=sem).all()
    print(papers)
    return render(request, 'courses/papers.html', {
        'papers': papers
    })

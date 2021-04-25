from django import http
from django.shortcuts import render, HttpResponse
from .models import Course, Paper, Year

# Create your views here.


def courses(request):
    # return HttpResponse("This is courses page")
    all_courses = Course.objects.all()
    # print(all_courses)
    context = {'allcourses': all_courses}

    return render(request, 'courses/courses.html', context)


def courses_post(request, slug):
    course = Course.objects.filter(slug=slug).first()
    context = {'course': course, 'sem':course.yearsOfCourse * 2}
    return render(request, 'courses/courses-details.html', context)


def show_papers(request, slug, sem):
    papers = Paper.objects.filter(course=slug, semester=sem).all()
    return render(request, 'courses/papers.html', {
        'papers': papers
    })


def display_papers(request, slug, semester, paperCode):
    paper_name = Paper.objects.filter(
        course=slug, semester=semester, paper_code=paperCode).first()
    avaliableYears = Year.objects.filter(paper_name=paper_name, course=slug).all()
    return render(request, 'courses/displayyear.html', {
        'papers': avaliableYears
    })

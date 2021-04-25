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
    print(slug, sem)
    papers = Paper.objects.filter(course=slug, semester=sem).all()
    return render(request, 'courses/papers.html', {
        'papers': papers
    })

def display_papers(request, slug, semester, slugshow):
    papers = Paper.objects.filter(course=slug, semester=semester, paperslug=slugshow).all()
    year = Year.objects.all()
    print(papers)
    return render(request, 'courses/displayyear.html', {'papers': papers, 'years': year})

def get_year(request, slug, sem, slugshow, year):
    years = Year.objects.filter(course=slug, paper_name=sem, paperslug=slugshow, year=year).all()
    print(years)
    return render(request, 'courses/year.html', {'year': years})

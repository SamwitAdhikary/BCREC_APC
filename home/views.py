from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return HttpResponse("This is about page")

def courses(request):
    return HttpResponse("This is courses page")

def contact(request):
    return HttpResponse("This is contact page")
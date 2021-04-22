from django.shortcuts import render, HttpResponse

# Create your views here.

def blog(request):
    return render(request, 'blog/blog.html')

def blogpost(request, slug):
    return render(request, 'blog/blogpost.html')
    # return HttpResponse(f"This is blog post of {slug}")

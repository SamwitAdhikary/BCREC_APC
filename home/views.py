from django.contrib import auth
from django.http.response import HttpResponseRedirect
import requests

from django.shortcuts import render, HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .send_email import sendEmail
from .models import Contact, UserProfileInfo, User, YoutubeVideos, Developers
from courses.models import Course


# Create your views here.
def get_data(endpoint):
    response = requests.get(endpoint)
    return response.json()

def checkUser(username):
    """ return True if user already have an account, otherwise False """
    return User.objects.filter(username=username).exists()


def index(request):
    allCourses = Course.objects.all()
    youtube_videos = YoutubeVideos.objects.all()
    # print(youtube_videos)
    developers = Developers.objects.all()
    # print(developers)

    if request.method == "POST":
        name = request.POST.get("name")
        if not checkUser(name):
            email = request.POST.get("email")
            password = request.POST.get("password")
            phNo = request.POST.get("phone")

            if email:
                verify_user(request, email, password)
                
                
                # user = User(
                #     username=name, password=make_password(request.POST.get("password")), email=email)
                # user.save()
                # if phNo:
                #     user_details = UserProfileInfo(user=user, phone_number=phNo)
                #     user_details.save()
                #     login(request, user)
            else:  
                user = authenticate(username=name, password=password)

                if user:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect(reverse('HomePage'))
                    else:
                        return HttpResponse("Account is not activated !")
                else:
                    print(f"Failed login, user-{name}, password-{password}")
                    return HttpResponse("Wrong Credentials !")
        else:
            return HttpResponse("You already have an account, Kindly Login IN !!")


    context = {
        'allcourses': allCourses,
        'yt_videos': youtube_videos,
        'developers': developers
        # 'developers': get_data('https://api.npoint.io/952ccba723fbe7772407')

    }

    return render(request, 'home/index.html', context)


def verify_user(request, email, password):
    if request.method == "POST":
        print(request, email, password)
        return render(request, 'home/verify-otp.html', {
            'email': email
        })



@login_required
def logoutUser(request):
   logout(request)
   return HttpResponseRedirect(reverse('HomePage'))

@login_required
def secret_page(request):
    return HttpResponse("You're Logged In !")

def about(request):
    return HttpResponse("This is about page")


def contact(request):
    if request.method == "POST":
        # fetch data from html Raw form
        name = request.POST.get("name")
        phNo = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to DB
        new_contact = Contact(name=name, email=email,
                              phone_number=phNo, message=message)
        new_contact.save()

        # Send mail
        # send_mail = sendEmail(user_name=name, user_email=email,
        #                       user_phone=phNo, user_msg=message)
        # send_mail.send()

    return render(request, 'home/contact.html')

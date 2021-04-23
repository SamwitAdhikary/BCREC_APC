from random import randint
from django.http.response import HttpResponseRedirect
import requests

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .send_email import sendEmail
from .models import Contact, UserProfileInfo, User, YoutubeVideos, Developers
from courses.models import Course
from django.contrib import messages

# CONSTANTS
OTP = None

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
    developers = Developers.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phNo = request.POST.get("phone")

        if email:
            if checkUser(name):
                return HttpResponse("You already have an account, Kindly Login IN !!")
            return verify_otp(request, email, name, make_password(password), phNo)
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
                messages.error(request, 'Wrong Credentials!!')
                
    context = {
        'allcourses': allCourses,
        'yt_videos': youtube_videos,
        'developers': developers
    }
    return render(request, 'home/index.html', context)


def verify_otp(request, email, name, password, phNo):
    global OTP
    if request.method == "POST":
        if not OTP:
            OTP = randint(1111, 9999)
            print(OTP)
            send_mail = sendEmail(user_name=name,user_email=email)
            send_mail.sendOtp(otp=OTP)
        else:
            user_otp = request.POST.get('otp')
            if user_otp and int(user_otp) == OTP:
                OTP = None
                user = User(username=name, password=password, email=email)
                user.save()
                if phNo:
                    user_details = UserProfileInfo(
                        user=user, phone_number=phNo)
                    user_details.save()
                login(request, user)
                return redirect('HomePage')
            OTP = None
            return HttpResponse("Wrong OTP, Try again ! <a href='/'>Back to Home</a>")

        return render(request, 'home/verify-otp.html', {
            'email': email, 'username': name, 'password': password, 'phNo': phNo
        })


@login_required
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('HomePage'))


@login_required
def secret_page(request):
    return HttpResponse("You're Logged In !")


def about(request):
    return render(request, 'home/about.html')


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

def overview(request):
    return HttpResponse("This is overview page")

def mission_and_vision(request):
    return HttpResponse("This is mission page")

def general_secretary_message(request):
    return HttpResponse('This is secretary message page')

def principal_message(request):
    return HttpResponse('This is principal message')

def approval_affiliation(request):
    return HttpResponse("This is approval message")

def collaboration(request):
    return HttpResponse('This is collaboration')

def committees(request):
    return HttpResponse('This is committees')

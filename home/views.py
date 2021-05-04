from email import message
from random import randint
from django.http.response import Http404, HttpResponseRedirect
import requests

from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .send_email import sendEmail
from .models import Contact, UserProfileInfo, User, YoutubeVideos, Developers
from courses.models import Course
from django.contrib import messages

from .forms import CreateUserFrom, UpdateForm, UpdateImageForm

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
    form = CreateUserFrom()

    if request.method == "POST":
        form = CreateUserFrom(request.POST)
        if not checkUser(form.data['username']):
            if form.is_valid():
                user = form.save()
                user.save()
                user_detils = UserProfileInfo(
                    user=user, autogen_otp=randint(100000, 999999))
                user_detils.save()
                login(request, user)
            else:
                if form.data['password1'] != form.data['password2']:
                    messages.error(request, 'Password Mismatched !')
                else:
                    messages.error(request, 'Password is too Easy to guess.')
        else:
            messages.error(
                request, "Sorry this username is not avaliable, please choose another one.")
    user = User.objects.filter(username=request.user).first()

    context = {
        'allcourses': Course.objects.all(), 'yt_videos': YoutubeVideos.objects.all(), 'developers': Developers.objects.all(),
        'form': form, 'profile': UserProfileInfo.objects.filter(user=user).first() if user else {}
    }
    return render(request, 'home/index.html', context)


@login_required
def verify_user(request):
    user = request.user
    user_info = UserProfileInfo.objects.filter(user=user).first()
    if not user_info.is_verify:
        sendLink = sendEmail(user_name=user, user_email=user.email)
        sendLink.sendOtp(
            f"http://127.0.0.1:8000/verify-otp/{user}/{user.email}/{user_info.autogen_otp}/{user.password}/")
        return render(request, 'home/verify.html', {
        })
    else:
        return render(request, 'home/success.html', {
            'msg': 'Your account is already verified !! Now you can all the features.'
        })


def verify_otp(request, username, email, password, otp):
    user = User.objects.filter(username=username).first()

    if user and user.email == email:
        userInfo = UserProfileInfo.objects.filter(user=user).first()
        if not userInfo.is_verify:
            if userInfo.autogen_otp == otp:
                UserProfileInfo.objects.filter(
                    user=user).update(is_verify=True)  # update to verify
                return render(request, 'home/success.html', {
                    'msg': 'Your account is verified successfully, Now you can use all the features.'
                })
        else:
            return render(request, 'home/success.html', {
                'msg': 'Your account is already verified !! Now you can all the features.'
            })

    return HttpResponse("Invalid !!")


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'home/profile.html', {
        'profile': UserProfileInfo.objects.filter(user=request.user).first()
    })


@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('HomePage'))


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


def loginUser(request):
    if request.method == "POST":
        user = authenticate(request=request, username=request.POST.get(
            'username'), password=request.POST.get('password'))
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('HomePage'))
        else:
            messages.error(request, 'Wrong Credentials!!')

        if user is not None:
            login(request, user)

    return render(request, 'home/login.html')


@login_required(login_url='/login/')
def update(request, pk):
    try:
        user = get_object_or_404(UserProfileInfo, autogen_otp=pk)
        # print(user)
    except Exception:
        raise Http404("Does not exist")

    if request.method == "POST":
        form = UpdateForm(request.POST, request.FILES, instance=user)
        # print(form.is_valid())

        if form.is_valid():
            form.save()
            messages.success(request, 'Updated')
            return redirect('/profile')
        else:
            messages.error(request, 'Not Saved')

    else:
        form = UpdateForm(instance=user)

    # print(form.errors)

    context = {'form': form}
    
    return render(request, 'home/update-profile.html', context)

    
@login_required(login_url='/login/')
def updateImage(request, pk):
    try:
        user = get_object_or_404(UserProfileInfo, autogen_otp=pk)
        # print(user)
    except Exception:
        raise Http404("Does not exist")

    if request.method == "POST":
        form = UpdateImageForm(request.POST, request.FILES, instance=user)
        # print(form.is_valid())

        if form.is_valid():
            form.save()
            messages.success(request, 'Updated')
            return redirect('/profile')
        else:
            messages.error(request, 'Not Saved')

    else:
        form = UpdateImageForm(instance=user)

    print(form.errors)

    context = {'form': form}
    
    return render(request, 'home/update-image.html', context)
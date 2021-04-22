from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name="BlogHomePage"),
    path("<str:slug>/", views.blogpost, name="BlogHomePage")
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name="CoursesPage"),
    path('<str:slug>', views.courses_post, name="CoursesPost"),
]

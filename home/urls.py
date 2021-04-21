from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="HomePage"),
    path('about', views.about, name="AboutPage"),
    path('courses', views.courses, name="CoursesPage"),
    path('contact', views.contact, name="ContactPage")
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name="CoursesPage"),
    path('<str:slug>/', views.courses_post, name="CoursesPost"),
    path('<str:slug>/<int:sem>/', views.show_papers, name="Papers"),
    path('<str:slug>/<int:semester>/<str:paperCode>/', views.display_papers),
]

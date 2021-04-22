"""
This Script is Used for populate something on the DB.
I fetched data from my old Json file, and added the courses to DB. 
Insted of doing it manually, I write a script for it. 
!Important --> Before run this script, Check your DB once, otherwise there will be a chance of,
Data redundancy.
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bcrecapc.settings')

import django
django.setup()

from courses.models import Courses
import requests


def add_Course(endpoint):
    response = requests.get(endpoint)
    courses = response.json()

    for course in courses:
        new_course = Courses.objects.get_or_create(
            slug=course['name'].lower(), title=course['name'], img_url=course['imgUrl'], description=course['full_name'], yearsOfCourse=course['yearsOfCourse']
            )[0]
        new_course.save()


if __name__ == "__main__":
    print("Added Users")
    add_Course('https://api.npoint.io/53897478e13604a83e77')
    print("Poplulating Complete")

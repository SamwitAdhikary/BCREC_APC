""" Script is used to scrap paper(course) data ..! """
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bcrecapc.settings')

import django
django.setup()

from bs4 import BeautifulSoup
import requests

from courses.models import Paper, Course


def select_course():
    course = Course.objects.filter(slug="mba").first()
    return course

def add_paper():
    for i in range(1, 9): # 9 is number of semester, loop will run 1-8 sem.
        response = requests.get(
            f'scrap-link/{i}')
        soup = BeautifulSoup(response.text, 'html.parser')
        paper_codes = soup.find_all("h3")
        paper_names = soup.find_all("h6")
        
        for j in range(len(paper_codes)-1):
            print(paper_names[j].getText())
            print(paper_codes[j].getText())
            paper = Paper.objects.get_or_create(
                paper_name=paper_names[j].getText(), paper_code=paper_codes[j].getText(), semester=i, course=select_course())[0]
            # paper.save() uncommant for save to DB
            

if __name__ == "__main__":
    print("Scripts Run !!!")
    # add_paper() # uncommant for run
    print("Complete, go to http://127.0.0.1:8000/admin/courses/paper/ for show the changes  !!")


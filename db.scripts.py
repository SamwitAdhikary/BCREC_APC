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

def test():
    response = requests.get(
        f'https://www.makaut.com/bca.html#list')
    soup = BeautifulSoup(response.text, 'html.parser')
    papers = soup.find_all("a")
    
    print(papers[0])

# def add_paper():
#     for i in range(1, 9): # 9 is number of semester, loop will run 1-8 sem.
#         for j in range(len(paper_codes)-1):
#             print(paper_names[j].getText())
#             print(paper_codes[j].getText())
#             paper = Paper.objects.get_or_create(
#                 paper_name=paper_names[j].getText(), paper_code=paper_codes[j].getText(), semester=i, course=select_course())[0]
#             # paper.save() uncomment for save to DB
            

if __name__ == "__main__":
    print("Scripts Run !!!")
    # add_paper() # uncommant for run
    test()
    print("Complete, go to http://127.0.0.1:8000/admin/courses/paper/ for show the changes  !!")


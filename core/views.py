 
from datetime import date
from typing import Counter
from student.models import Student
from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from events.models import Events

# Create your views here.

def home(request):
    student=Student.objects.count()
    trainer=Trainer.objects.count()
    courses=Courses.objects.count()
    events=Events.objects.count()

    data = {"student": student, "trainer": trainer, "course": courses ,"events":events}
    return render(request, "home_page.htm", data)


from django.shortcuts import render

# Create your views here.

from .forms import CoursesRegistrationForm
from .models import Courses


def register_courses(request):
    form = CoursesRegistrationForm()
    return render(request,"register-courses.html",{"form":form})

def register_courses(request):
    if request.method == "POST":
        form=CoursesRegistrationForm(request.POST)
        if form .is_valid():
            form.save()
        else:
            print(form.errors)
    else:
            form=CoursesRegistrationForm()
    return render(request,'register-courses.html',{"form":form})

def courses_list(request):
    courses = Courses.objects.all()
    return render(request,"courses-list.html",{'courses':courses})



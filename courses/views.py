from django.shortcuts import render

# Create your views here.

from .forms import CoursesRegistrationForm


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


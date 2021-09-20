
from .models import Courses
from django.shortcuts import redirect, render
from.forms import CourseRegistrationForm

# Create your views here.

def register_courses(request):
    if request.method=="POST":
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_courses')
        else:
            print(form.errors)
    else:
        form = CourseRegistrationForm()

    return render(request, "register_courses.htm", {"form":form})

def course_list(request):
    courses = Courses.objects.all()
    return render(request, "course_list.htm", {"courses":courses})


def edit_course(request, id):
    courses = Courses.objects.get(id=id)
    if request.method == "POST":
        form = CourseRegistrationForm(request.POST, instance=courses)
        if form.is_valid():
            form.save()
        return redirect("course_list")
       
    else:
        form = CourseRegistrationForm(instance=courses)     
        return render(request, "edit_course.htm", {"form":form})       


def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("course_list")
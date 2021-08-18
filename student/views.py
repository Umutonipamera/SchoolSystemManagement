from django.shortcuts import render

# Create your views here.

from .forms import StudentRegistrationForm
from .models import Student
# Create your views here.

def register_student(request):
    form = StudentRegistrationForm()
    return render(request,"register-student.html",{"form":form})

def register_student(request,):
    if request.method == "POST":
        form=StudentRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
            form=StudentRegistrationForm()
    return render(request,'register-student.html',{"form":form})
def student_list(request):
    students = Student.objects.all()
    return render(request,"student-list.html",{'students':students})


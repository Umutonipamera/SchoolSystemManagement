from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from events.models import Events
from .serializers import StudentSerializer
from .serializers import TrainerSerializer
from .serializers import CoursesSerializer
from .serializers import EventsSerializer



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
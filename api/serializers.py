
from rest_framework import serializers
from student .models import Student
from trainer .models import Trainer
from courses .models import Courses
from events .models import Events


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("first_name","last_name","age")

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ("first_name","last_name","age")

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ("course_name","course_id","course_trainer")

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("event_name","event_location","start_time")
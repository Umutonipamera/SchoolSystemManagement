from django.db import models

# Create your models here.

class Courses (models.Model):
       course_name=models.CharField(max_length=12)
       trainer=models.CharField(max_length=20)
       trainer_id=models.CharField(primary_key=True,max_length=20)
       syllabus=models.FileField(upload_to='documents/%y/%m/%d',null=True)
       course_code=models.CharField(max_length=12)
       description=models.TextField()


     
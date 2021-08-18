from django.db import models
import datetime
from django.core.validators import MaxValueValidator,MinValueValidator
#import phone number




def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)




class Student (models.Model):
       first_name=models.CharField(max_length=12)
       last_name=models.CharField(max_length=20)
       age=models.PositiveSmallIntegerField()
       date_of_birth=models.DateField(null=True)

       NATIONALITY=(
           ("Kenyan","Kenyan"),
           ("Ugandan","Ugandan"),
           ("Rwandan","Rwandan"),
           ("South Sudanese","South Sudanese"),
       )
       nationality=models.CharField(max_length=20,choices= NATIONALITY, default='Kenyan')
       GENDER=(
           ("Male","Male"),
           ("Female","Female"),
           ("Non-Binary","Non-Binary"),
           ("Transgender","Transgender"),
        )
       gender=models.CharField(max_length=12,choices=GENDER, default='Female')
       id=models.CharField(primary_key=True,max_length=20)
       email=models.EmailField(null=True)
       phoneNumber=models.CharField(max_length=16,null=True)
       medicalReport=models.FileField(upload_to='documents/%y/%m/%d',null=True)
       admissionDate=models.DateField(default='yyyy-mm-dd')
       academic_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984),max_value_current_year])

       CITY=(
           ("Nairobi","Nairobi"),
           ("Kampala","Kampala"),
           ("Kigali","Kigali"),
           ("kartum","Kartum"),
        )

       city =models.CharField(max_length=12,choices=CITY,default="Nairobi")
       guadian_name=models.CharField(max_length=20,null=True)
       guadian_phoneNumber=models.CharField(max_length=16,null=True)
       profile_picture=models.ImageField(upload_to="images|",null=True)
       
      
       




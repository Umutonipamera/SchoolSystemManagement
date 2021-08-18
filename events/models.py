from django.db import models

# Create your models here.

import datetime
from django.core.validators import MaxValueValidator,MinValueValidator
#import phone number





class Events (models.Model):
       event_name=models.CharField(max_length=12)
       location=models.CharField(max_length=12)
       date_of_event=models.DateField(default='dd-mm-yyyy')
       start_duration=models.DurationField()
       end_duration=models.DurationField()
       link_of_the_event=models.CharField(max_length=200)
       description=models.TextField()
      
      
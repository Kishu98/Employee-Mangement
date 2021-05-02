from django.db import models
import datetime


# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='images/', blank=True)
    date = models.DateField(("Date of Joining"), default=datetime.date.today)
    GENDER = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    gender = models.CharField(max_length=1, choices=GENDER, null=True)
    

    
    

from django.db import models

# Create your models here.



class school(models.Model):
    school_id=models.IntegerField()
    school_name=models.CharField(max_length=100)  
    student_name=models.CharField(max_length=100)  

class student(models.Model):
    student_id=models.IntegerField()
    student_name=models.CharField( max_length=50)
    school_id=models.IntegerField()
    start_date=models.DateTimeField()
    due_date=models.DateTimeField()
    freq_month=models.IntegerField()
    amount=models.IntegerField()
    defaultor=models.IntegerField(default=0)

class transaction(models.Model):
    transaction_id=models.IntegerField()
    student_id=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateTimeField()   



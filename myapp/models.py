from django.utils import timezone
from django.db import models

class designationModel(models.Model):
    title=models.CharField(max_length=100,unique=True)
    HRA_percent=models.FloatField(max_length=100,unique=True)
    DA_percent=models.FloatField(default=0)
    TA_percent=models.FloatField(default=0)

    def __str__(self):
        return self.title

class employeeModel(models.Model):
    emp_name=models.CharField(max_length=100,null=True)
    emp_id=models.IntegerField(null=True)
    emp_city=models.CharField(max_length=100,null=True)
    emp_gender=models.CharField(max_length=100,null=True)
    emp_DOB=models.DateField(null=True,blank=True)
    emp_email=models.EmailField(unique=True)
    emp_phone=models.CharField(max_length=15, null=True)
    emp_address=models.TextField(blank=True,null=True)
    basic_salary=models.FloatField(max_length=100,null=True)
    designation=models.ForeignKey(designationModel,on_delete=models.CASCADE,null=True)
    bonus=models.FloatField(max_length=100,null=True,default=0)
    overtime=models.FloatField(max_length=100,null=True,default=0)
    salary=models.FloatField(max_length=100,null=True,default=0)
    date_of_joining=models.DateField(default=timezone.now)
    emp_photo=models.ImageField(upload_to='photos/',null=True,blank=True)


   

    



    

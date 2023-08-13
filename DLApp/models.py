from django.db import models
class Employee(models.Model):
    empNo=models.CharField(max_length=20)
    empName=models.CharField(max_length=20)

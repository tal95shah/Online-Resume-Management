from django.db import models

# Create your models here.


class Designation(models.Model):
        DesignationName=models.CharField(max_length=30);
        Status = models.CharField(max_length=30);



def __str__(self):
        return self.DesignationName

class HRManager(models.Model):
        HRName=models.CharField(max_length=30);
        age = models.CharField(max_length=30);



class Department(models.Model):
        Departnemt_Name=models.CharField(max_length=30);
        HRManager=models.CharField(max_length=30);

class Offices(models.Model):
        Offices_Name = models.CharField(max_length=30);
        HRManager = models.CharField(max_length=30);
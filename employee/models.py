from django.db import models
from django.contrib.auth.models import User

class Superadmin(models.Model):
    added_date = models.DateTimeField(auto_now_add=True,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200,null= True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=12, null=True)
    password = models.CharField(max_length=20, null=True)
    
    def isExists(self):
        if Superadmin.objects.filter(email = self.email):
            return True
        return  False

class Employee(models.Model):
    added_date = models.DateTimeField(auto_now_add=True,null=True)
    name = models.CharField(max_length=200,null= True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=12, null=True)
    gender = models.CharField(max_length=20, null=True)
    
    def isExists(self):
        if Employee.objects.filter(email = self.email):
            return True
        return  False
from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserAccount



# class Department(models.Model):
#     department_name=models.CharField(max_length=100, unique=True)
#     slug=models.SlugField(max_length=100, unique=True)
#     description=models.TextField(max_length=300, blank=True)
    
#     # def __str__(self) -> str:
#     #     return self.department_name
    


class Course(models.Model):
    course_title=models.CharField(max_length=100)
    course_description=models.TextField()
    department=models.CharField(max_length=100)
    created_date= models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.course_title
    
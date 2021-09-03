from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TeachersDesignation(models.Model):
    designation = models.CharField(max_length=40)
    def __str__(self):
        return self.designation


class TeachersDepartment(models.Model):
    department = models.CharField(max_length=40)
    def __str__(self):
        return self.department

class TeachersFaculty(models.Model):
    faculty = models.CharField(max_length=40)
    def __str__(self):
        return self.faculty

class TeachersList(models.Model):
    userId = models.OneToOneField(User,on_delete=models.CASCADE)
    teacher = models.BooleanField(default=True)
    empid = models.IntegerField()
    designation = models.ForeignKey(TeachersDesignation, on_delete=models.CASCADE)
    department = models.ForeignKey(TeachersDepartment, on_delete=models.CASCADE,null=True,default='')
    faculty = models.ForeignKey(TeachersFaculty, on_delete=models.CASCADE,null=True,default='')
    personalWebPage = models.URLField(null=True,default='')
    phone = models.IntegerField(null=True)

    def __str__(self):
        return str(self.empid)


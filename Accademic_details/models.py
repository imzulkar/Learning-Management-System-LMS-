from django.db import models

# Create your models here.
class Course(models.Model):
    courseCode = models.CharField(max_length=10)
    courseTitle = models.CharField(max_length=40)
    courseCredit = models.IntegerField()

    def __str__(self):
        return self.courseCode

class Semester(models.Model):
    semester = models.CharField(max_length=30)
    def __str__(self):
        return self.semester
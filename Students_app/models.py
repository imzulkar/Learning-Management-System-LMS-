from django.db import models
from django.contrib.auth.models import User
from Teachers_app.models import TeachersList
from Accademic_details.models import Course,Semester
# Create your models here.

class StudentsInfo(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    studentID = models.IntegerField()
    student = models.BooleanField(default=True)
    father_name = models.CharField(max_length=40)
    mother_name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return str(self.studentID)

class MarksDistribution(models.Model):
    student = models.ForeignKey(StudentsInfo,on_delete=models.CASCADE)
    quiz_1 = models.IntegerField(default=0)
    quiz_2 = models.IntegerField(default=0)
    quiz_3 = models.IntegerField(default=0)
    Assignment = models.IntegerField(default=0)
    presentation = models.IntegerField(default=0)
    mid = models.IntegerField(default=0)
    final = models.IntegerField(default=0)
    mid_improvement = models.IntegerField(default=0)
    teacher = models.ForeignKey(TeachersList,on_delete=models.CASCADE)

    def __str__(self):
        avg =str((self.quiz_1+self.quiz_2+self.quiz_3)/3)
        sid = str(self.student)
        return 'Quid Avg:'+avg +'----ID:'+ sid

class RegisteredCourse(models.Model):
    student = models.ForeignKey(StudentsInfo,on_delete=models.CASCADE)
    registeredCourse = models.ForeignKey(Course,on_delete=models.CASCADE)
    registeredSemester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    # info = str(student) + ' '+ str(registeredCourse)+ ' '+str(registeredSemester)
    def __str__(self):
        template = '{0.student}, {0.registeredCourse}, {0.registeredSemester}'
        return template.format(self)
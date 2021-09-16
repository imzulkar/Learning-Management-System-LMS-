from django.forms import ModelForm
from Teachers_app.models import TeachersList
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import StudentsInfoModel

class TeachersInfoForm(ModelForm):
    class Meta:
        model= TeachersList
        exclude = ['userId','teacher']


class AddTeacherForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
        help_texts = {
            'username': None,
            'password2':None,
        }


class AddNewStudentsForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1', 'password2')
        help_texts = {
            'username': None,
            'password':None,
        }

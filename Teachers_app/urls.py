from django.contrib import admin
from django.urls import path
from Teachers_app import views

app_name = 'Teachers_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.TeacherAuthentication,name='teacherslogin'),
    path('dashboard/',views.TeachersDashboard,name='teachers_dashboard'),
    path('register/',views.NewStudentRegistration,name='student_register'),
    path('logout/',views.TeacherLogout,name='logout'),
    path('profile/',views.TeachersProfile, name='teaches_profile'),




]
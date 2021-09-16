from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView,UpdateView,TemplateView,ListView,DetailView
from django.views.generic.edit import FormMixin
from .models import Course,OfferedCourse,Semester
from Teachers_app.models import TeachersList
from django.contrib.auth.models import User
from .forms import TeachersInfoForm,AddTeacherForm

# Create your views here.
class SubjectListView(ListView):
    context_object_name = 'subjects_list'
    model = Course
    template_name = 'Admin_panel/course_list'

class AddCourseView(CreateView):
    context_object_name = 'addcourse'
    model = Course
    fields = ['courseCode','courseTitle','courseCredit']
    template_name = 'Admin_panel/add_course.html'

class UpdateCourseView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'Admin_panel/add_course.html'


class DeleteCourseView(DeleteView):
    model = Course
    success_url = reverse_lazy('Admin_panel:course_list')
    template_name = 'Admin_panel/delete_subject.html'


# Teachers Section
class TeacherListView(ListView):
    context_object_name = 'teachers_list'
    model = User
    queryset = User.objects.filter(teachers_info__teacher = True)
    template_name = 'Admin_panel/teachers_list.html'

class TeacherDetailView(DetailView):
    model = User
    context_object_name = 'teacher_details'
    template_name = 'Admin_panel/detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']

        data = TeachersList.objects.get(userId__pk=pk)
        print(data.teacher, data.empid)

        context['teachers_info'] = data
        return context

# class AddNewTeacher(CreateView):
#     model = User
#     fields = ['username','first_name','last_name','email', 'password']
#     template_name = 'Admin_panel/add_teacher.html'
#
#
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#
#         if (self.request =='POST'):
#             print('if ok')
#             form2 = TeachersInfoForm(self.request.POST)
#             print(form2)
#             if form2.is_valid():
#                 form2.userId = User
#                 print(form2.userId)
#                 form2.save()
#         else:
#             form2 = TeachersInfoForm()
#             context['form2'] = form2
#         context['form2'] = form2
#
#
#         return context


def AddNewTeacherView(request):
    if request.method=='POST':
        form = AddTeacherForm(data=request.POST)
        form2 = TeachersInfoForm(data=request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            # user.set_password(user.password)
            user.save()
            user_info = form2.save(commit=False)
            user_info.userId = user
            user_info.save()
    else:
        form = AddTeacherForm()
        form2 = TeachersInfoForm()

    return render(request,'Admin_panel/add_teacher.html',context={'form':form,'form2':form2})


# def AddNewStudentsView(request):
#     if request.method=='POST':
#         form = AddNewStudentsForm(data=request.POST)
#         form2 = StudentsInfoForm(data=request.POST)
#         if form.is_valid() and form2.is_valid():
#             user = form.save()
#             user.set_password(user.password)
#             user.save()
#             user_info = form2.save(commit=False)
#             user_info.userId = user
#             user_info.save()
#     else:
#         form = AddNewStudentsForm()
#         form2 = StudentsInfoForm()
#
#     return render(request,'Admin_panel/add_teacher.html',context={'form':form,'form2':form2})
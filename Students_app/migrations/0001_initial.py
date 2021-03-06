# Generated by Django 3.2.4 on 2021-09-14 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Teachers_app', '0001_initial'),
        ('Admin_panel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.IntegerField()),
                ('student', models.BooleanField(default=True)),
                ('father_name', models.CharField(blank=True, max_length=40)),
                ('mother_name', models.CharField(blank=True, max_length=40)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('dateOfBirth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('religion', models.CharField(blank=True, max_length=20)),
                ('nationality', models.CharField(blank=True, max_length=20)),
                ('nationalId', models.IntegerField(blank=True, null=True)),
                ('userId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registeredCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin_panel.course')),
                ('registeredSemester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin_panel.semester')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students_app.studentsinfo')),
            ],
        ),
        migrations.CreateModel(
            name='MarksDistribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_1', models.IntegerField(default=0)),
                ('quiz_2', models.IntegerField(default=0)),
                ('quiz_3', models.IntegerField(default=0)),
                ('Assignment', models.IntegerField(default=0)),
                ('presentation', models.IntegerField(default=0)),
                ('mid', models.IntegerField(default=0)),
                ('final', models.IntegerField(default=0)),
                ('mid_improvement', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students_app.studentsinfo')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teachers_app.teacherslist')),
            ],
        ),
    ]

# Generated by Django 3.2.4 on 2021-09-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferedCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=30)),
                ('courseCredit', models.IntegerField()),
                ('courseGraduationYear', models.IntegerField()),
                ('courseCost', models.IntegerField()),
            ],
        ),
    ]

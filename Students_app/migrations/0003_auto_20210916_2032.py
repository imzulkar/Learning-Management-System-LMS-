# Generated by Django 3.2.4 on 2021-09-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students_app', '0002_studentfeedbackmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentfeedbackmodel',
            name='feedback',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='studentfeedbackmodel',
            name='header',
            field=models.CharField(default='', max_length=200),
        ),
    ]

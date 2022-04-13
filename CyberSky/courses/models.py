from django.db import models

# Create your models here.
from django.utils.html import format_html


class Instructor(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    payment = models.FloatField(null=True)
    salary = models.FloatField(null=True)

    def share_percentage(self):
        if self.salary and self.payment:
            percentage = round((self.payment / self.salary * 100), 2)
        else:
            percentage = 0
        return format_html(''' 
            <progress value="{0}" max="100"></progress>
            <span style="font-weight:bold">{0}%</span>
            ''', percentage)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    about_course = models.TextField()

    def __str__(self):
        return self.course_name


import datetime
from django.db import models
from django.utils import timezone

class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate')]

    Student_ID = models.IntegerField(unique = True)
    Password = models.CharField(max_length = 20)
    Username = models.CharField(max_length = 20, unique = True)
    Class_Standing = models.CharField(max_length = 2, choices = YEAR_IN_SCHOOL_CHOICES)
    Phone_Number = models.CharField(max_length = 14)

    def __str__(self):
        return self.Username


class Subject(models.Model):
    title = models.CharField(max_length = 40)


class Course(models.Model):
    sub = models.CharField(max_length = 40) # this field is title from Subject
    crn = models.IntegerField()
    Instructor = models.CharField(max_length= 30)
    Title = models.CharField(max_length=20)
    cnum = models.CharField(verbose_name = 'Course Number', max_length = 15)
    Actv = models.CharField(verbose_name = "Type of class", max_length = 15)
    Units = models.IntegerField(default= 0)
    Days =  models.CharField(max_length = 10)
    TimeOfLec = models.CharField(max_length=10)
    Bldg_Rm = models.CharField(max_length = 20, default = "REMOTE ONLY")
    Start = models.CharField(max_length=10)
    End = models.CharField(max_length=10)
    Max_enrl = models.IntegerField()
    Act_enrl = models.IntegerField()
    Seats_avil = models.IntegerField()

class Rollcall(models.Model):
    course = models.CharField(max_length = 15) # this field is cnum from Course
    student = models.IntegerField() # this field is student id from Student



class Requirments(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    cs1 = models.CharField(max_length = 20, verbose_name = "Class Standing 1")
    cs2 = models.CharField(max_length = 20)
    cs3 = models.CharField(max_length = 20)
    cs4 = models.CharField(max_length = 20)
    pr1 = models.CharField(max_length = 20)
    pr2 = models.CharField(max_length = 20)
    pr3 = models.CharField(max_length = 20)
    pr4 = models.CharField(max_length = 20)
    pr5 = models.CharField(max_length = 20)
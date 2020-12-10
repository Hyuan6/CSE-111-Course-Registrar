
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
    Academic_Probation_Hold = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.Username


class Subject(models.Model):
    title = models.CharField(max_length = 40)


class Course(models.Model):
    # this field is title from Subject
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

class Roll(models.Model):
    course = models.CharField(max_length = 15) # this field is cnum from Course
    student = models.IntegerField() # this field is student id from Student
    grade = models.CharField(max_length = 5, blank=True, null=True)



class Requirments(models.Model):
    course = models.CharField(max_length=15)
    cs1 = models.CharField(max_length = 20, verbose_name = "Class Standing 1")
    cs2 = models.CharField(max_length = 20, blank=True, null=True)
    cs3 = models.CharField(max_length = 20, blank=True, null=True)
    cs4 = models.CharField(max_length = 20, blank=True, null=True)
    pr1 = models.CharField(max_length = 20, blank=True, null=True)
    pr2 = models.CharField(max_length = 20, blank=True, null=True)
    pr3 = models.CharField(max_length = 20, blank=True, null=True)
    pr4 = models.CharField(max_length = 20, blank=True, null=True)
    pr5 = models.CharField(max_length = 20, blank=True, null=True)

class Honors(models.Model):
    student_id = models.IntegerField()
    honor_name = models.CharField(max_length=20, blank=True, null=True)
    semester_awarded = models.CharField(max_length=20, blank=True, null=True)

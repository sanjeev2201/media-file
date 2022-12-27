from django.db import models
from .choices import state_choices
# Create your models here.
class CommonInfo(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    state=models.CharField(choices=state_choices,max_length=50)
    age=models.PositiveBigIntegerField()
    class Meta:
        abstract = True
class Teacher(CommonInfo):
    salary  = models.FloatField()
    Photo=models.ImageField(upload_to='teacherimg')
    class Meta:
        ordering = ('name',)
        db_table = 'Teacher'

class Student(CommonInfo):
    dob = models.DateField()
    job_location=models.CharField(max_length=200)
    Photo=models.ImageField(upload_to='studentimg')
    Resume=models.FileField(upload_to='rdoc')
    class Meta:
        ordering = ('age',)
        db_table = 'Student'

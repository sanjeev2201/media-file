from django import forms
from .choices import GENDER_CHOICES,JOB_CHOICES
from .models import Teacher,Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1', 'password2')
        
class TeacherForm(forms.ModelForm):
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER_CHOICES))
    class Meta:
        model=Teacher
        fields='__all__'
class StudentForm(forms.ModelForm):
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER_CHOICES))
    job_location = forms.CharField(widget = forms.CheckboxSelectMultiple(choices=JOB_CHOICES))
    class Meta:
        model=Student
        fields='__all__'
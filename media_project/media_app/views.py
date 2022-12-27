from django.shortcuts import render,redirect
from .forms import TeacherForm,StudentForm
from .models import Teacher,Student
import datetime
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'myapp/base.html')
    
  
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher-list')
    else:
        form = TeacherForm()
        context = {
            'form':form,
        }
    return render(request,'myapp/createteacher.html',context)

def Teacher_list(request):
    teachers=Teacher.objects.all()
    return render(request,'myapp/teacher_list.html',{'teachers':teachers})

def teacher_edit(request,pk):
    teacher = Teacher.objects.get(id=pk)
    form = TeacherForm(instance=teacher)

    if request.method == 'POST':
        form =TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher-list')

    context = {
        'teacher': teacher,
        'form': form,
    }
    return render(request, 'myapp/teacheredit.html', context)


def teacher_delete(request,pk):
    teacher = Teacher.objects.get(id=pk)

    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher-list')

    context = {
        'teacher': teacher,
    }
    return render(request, 'myapp/teacherdelete.html', context)


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            ag=form.cleaned_data.get('age')
            if ag < 35:
                form.save()
                messages.success(request, 'New Profile added')
                return redirect('student-list')
            else:
                messages.warning(request, 'age should be less than than 35')
                
    else:
        form = StudentForm()
    return render(request,'myapp/createstudent.html',{'form':form})

def Student_list(request):
    students=Student.objects.all()
    today_date=datetime.date.today
    return render(request,'myapp/student_list.html',{'students':students,'date':today_date})
from django.shortcuts import render,redirect
from .forms import TeacherForm,StudentForm
from .models import Teacher,Student
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
# Create your views here.

def index_page(request):
    return render(request,'myapp/index.html')

@login_required(login_url='index')#url name
def home_page(request):
    return render(request,'myapp/base.html')

#login request

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                print(user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                print('User not found')
                messages.error(request,"No login credentials found")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request,'myapp/login.html',{'form':form})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']    
            pass1=form.cleaned_data['password1']
            pass2=form.cleaned_data['password2']
            form.save()
            user=auth.authenticate(username=username,password=pass1)
            auth.login(request,user)
            messages.info(request,'Account created successfully!!')
            return redirect('login')
    else:
        form = SignUpForm()       
    return render(request,'myapp/signup.html',{'form':form})

def logout(request):
        auth.logout(request)
        messages.info(request, "You have successfully logged out.")
        return  redirect('index')
    
def user_list(request):
    users=User.objects.all()
    return render(request,'myapp/user_list.html',{'users':users})
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
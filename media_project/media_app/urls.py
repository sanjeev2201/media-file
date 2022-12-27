from django.urls import path
from . import views
urlpatterns = [
    path('crstudent/',views.create_student,name='createstudent'),
    path('crteacher/',views.create_teacher,name='createteacher'),
    path('studentlist/',views.Student_list,name='student-list'),
    path('teacherlist/',views.Teacher_list,name='teacher-list'),
    path('teacheredit/<int:pk>',views.teacher_edit,name='teacher-edit'),
    path('teacherdelete/<int:pk>',views.teacher_delete,name='teacher-delete')
]
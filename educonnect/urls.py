from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('index1/',views.index1,name='index1'),
    path('index1/register/',views.register,name='register'),
    path('index1/register/addstudent',views.addstudent,name='addstudent'),
    path('register/',views.register,name='register'),
    path('register/addstudent',views.addstudent,name='addstudent'),

    path('logout/',views.logout,name='logout'),
    path('login/',views.login,name='login'),
    path('login/addlogin',views.addlogin,name='addlogin'),
    path('register_faculty',views.register_faculty,name='register_faculty'),
    path('addfaculty',views.addfaculty,name='addfaculty'),
    path('view_students_admin',views.view_students_admin,name='view_students_admin'),
    path('approve_stud/<int:id>',views.approve_stud,name='approve_stud'),
    path('reject_stud/<int:id>',views.reject_stud,name='reject_stud'),
    

    path('assign',views.assign,name='assign'),
    path('addassign',views.addassign,name='addassign'),
    path('view_faculty_admin',views.view_faculty_admin,name='view_faculty_admin'),
    path('remove_fac/<int:id>',views.remove_fac,name='remove_fac'),

    path('profile',views.profile,name='profile'),
    path('class_schedule',views.class_schedule,name='class_schedule'),
    path('addschedule',views.addschedule,name='addschedule'),
    path('viewclass',views.viewclass,name='viewclass'),
    path('apply_leave',views.apply_leave,name='apply_leave'),
    path('addapply_leave',views.addapply_leave,name='addapply_leave'),
    path('view_leave_status',views.view_leave_status,name='view_leave_status'),
    path('stud_profile',views.stud_profile,name='stud_profile'),
    path('leave_request',views.leave_request,name='leave_request'),
    path('admin_viewleave',views.admin_viewleave,name='admin_viewleave'),
    path('admin_viewclass',views.admin_viewclass,name='admin_viewclass'),

    path('approve_leave/<int:id>',views.approve_leave,name='approve_leave'),
    path('reject_leave/<int:id>',views.reject_leave,name='reject_leave'),

    path('course',views.course,name='course'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('view_course',views.view_course,name='view_course'),
    path('assign_course/<int:id>',views.assign_course,name='assign_course'),
    path('assign_course/addassign_course',views.addassign_course,name='addassign_course'),

    path('view_assign_course',views.view_assign_course,name='view_assign_course'),
    path('stud_profile_up',views.stud_profile_up,name='stud_profile_up'),
    path('addstudent_up/<int:id>',views.addstudent_up,name='addstudent_up'),
    path('profile_up',views.profile_up,name='profile_up'),
    path('addfaculty_up/<int:id>',views.addfaculty_up,name='addfaculty_up'),
    path('c_payment/<int:id>',views.c_payment,name='c_payment'),
    path('c_payment/addpayment',views.addpayment,name='addpayment'),
    path('success',views.success,name='success'),
    path('view_payments',views.view_payments,name='view_payments'),
    path('viewpayments',views.viewpayments,name='viewpayments'),
    path('my_class_schedule',views.my_class_schedule,name='my_class_schedule'),

    path('edit_class/<int:id>',views.edit_class,name='edit_class'),
    path('edit_class/edit_class_up/<int:id>',views.edit_class_up,name='edit_class_up'),



    path('add_stdy_mtr',views.add_stdy_mtr,name='add_stdy_mtr'),
    path('stdy_mtr',views.stdy_mtr,name='stdy_mtr'),
    path('view_stdy_mtr',views.view_stdy_mtr,name='view_stdy_mtr'),
    path('view_mystudents',views.view_mystudents,name='view_mystudents'),
    path('view_stdy_mtr_fclty',views.view_stdy_mtr_fclty,name='view_stdy_mtr_fclty'),

    path('chatuser',views.chatuser,name='chatuser'),
    path('addchat_std',views.addchat_std,name='addchat_std'),
    path('chatmentor/<int:id>',views.chatmentor,name='chatmentor'),
    path('chatmentor/addchat_mnt',views.addchat_mnt,name='addchat_mnt'),
    path('progress',views.progress,name='progress'),
    path('certificate/', views.certificate, name='certificate'),
    path('signlanguage/', views.signlanguage, name='signlanguage'),




    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

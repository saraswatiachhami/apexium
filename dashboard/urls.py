from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('collaboration/', views.collaboration, name='collaboration'),

    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_add, name='course_add'),
    path('courses/edit/<int:id>/', views.course_edit, name='course_edit'),
    path('courses/delete/<int:id>/', views.course_delete, name='course_delete'),

    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/edit/<int:id>/', views.student_edit, name='student_edit'),
    path('students/delete/<int:id>/', views.student_delete, name='student_delete'),


    path('dashboard/students/add/', views.student_add, name='student_add'),


    path('staff/', views.staff_list, name='staff_list'),
    path('staff/add/', views.staff_add, name='staff_add'),
    path('staff/edit/<int:id>/', views.staff_edit, name='staff_edit'),
    path('staff/delete/<int:id>/', views.staff_delete, name='staff_delete'),

    path('instructors/', views.instructor_list, name='instructor_list'),

    path('dashboard/instructors/', views.instructor_list, name='instructor_list'),
    path('dashboard/instructors/add/', views.instructor_add, name='instructor_add'),
    path('dashboard/instructors/edit/<int:id>/', views.instructor_edit, name='instructor_edit'),
    path('dashboard/instructors/delete/<int:id>/', views.instructor_delete, name='instructor_delete'),
]







from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.school_login, name='school_login'),
    path('dashboard/', views.school_dashboard, name='school_dashboard'),
    path('students/', views.view_students, name='view_students'),
    path('students/<int:student_id>/feedback/', views.submit_school_feedback, name='submit_school_feedback'),
]

# school_supervisor/urls.py
from django.urls import path
from . import views

app_name = 'school_supervisor'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.students, name='students'),
    path('students/<int:student_id>/feedback/', views.feedback, name='feedback'),
    path('logout/', views.logout, name='logout'),
]

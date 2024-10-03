from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.industry_login, name='industry_login'),
    path('dashboard/', views.industry_dashboard, name='industry_dashboard'),
    path('students/', views.view_students, name='view_students'),
    path('students/<int:student_id>/feedback/', views.submit_feedback, name='submit_feedback'),
]

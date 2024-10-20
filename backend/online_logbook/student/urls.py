from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.student_login, name='student_login'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logbook/', views.fill_daily_log, name='fill_daily_log'),
    path('form/', views.fill_student_form, name='fill_student_form'),
    path('news/', views.news, name='fill_student_form'),
    path('logout/', views.view_industry_feedback, name='view_industry_feedback'),
    # path('view-feedback/school/', views.view_school_feedback, name='view_school_feedback'),
]

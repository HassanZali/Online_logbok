from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logbook/', views.logbook, name='logbook'),
    path('form/', views.form_view, name='form'),
    path('news/', views.news, name='news'),
    path('logout/', views.logout, name='logout'),
]

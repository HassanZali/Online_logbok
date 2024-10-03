from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import DailyLogForm, StudentForm
from industry_supervisor.models import IndustryFeedbackForm
from school_supervisor.models import SchoolFeedbackForm


def daily_log_view(request):
    if request.method == 'POST':
        form = DailyLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:dashboard')  # Redirect to the student dashboard after submission
    else:
        form = DailyLogForm()
    return render(request, 'student/daily_log.html', {'form': form})

def student_profile_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=request.user.student)
        if form.is_valid():
            form.save()
            return redirect('student:profile')  # Redirect to profile page
    else:
        form = StudentForm(instance=request.user.student)
    return render(request, 'student/profile.html', {'form': form})



def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_dashboard')
        else:
            return render(request, 'student/login.html', {'error': 'Invalid login credentials'})
    return render(request, 'student/login.html')

def student_dashboard(request):
    return render(request, 'student/dashboard.html')

def fill_daily_log(request):
    if request.method == 'POST':
        form = DailyLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.student = request.user.student
            log.save()
            return redirect('student_dashboard')
    else:
        form = DailyLogForm()
    return render(request, 'student/daily_log.html', {'form': form})

def fill_student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_form = form.save(commit=False)
            student_form.student = request.user.student
            student_form.save()
            return redirect('student_dashboard')
    else:
        form = StudentForm()
    return render(request, 'student/student_form.html', {'form': form})

def view_industry_feedback(request):
    feedback = IndustryFeedbackForm.objects.filter(student=request.user.student)
    return render(request, 'student/view_industry_feedback.html', {'feedback': feedback})

def view_school_feedback(request):
    feedback = SchoolFeedbackForm.objects.filter(student=request.user.student)
    return render(request, 'student/view_school_feedback.html', {'feedback': feedback})

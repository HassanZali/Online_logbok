from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import SchoolSupervisor
from student.models import Student
from .forms import SchoolFeedbackForm

def school_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('school_dashboard')
        else:
            return render(request, 'school_supervisor/login.html', {'error': 'Invalid login credentials'})
    return render(request, 'school_supervisor/login.html')

def school_dashboard(request):
    return render(request, 'school_supervisor/dashboard.html')

def view_students(request):
    supervisor = request.user.schoolsupervisor
    students = Student.objects.filter(school_supervisor=supervisor)
    return render(request, 'school_supervisor/view_students.html', {'students': students})

def submit_school_feedback(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = SchoolFeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.student = student
            feedback.school_supervisor = request.user.schoolsupervisor
            feedback.save()
            return redirect('school_dashboard')
    else:
        form = SchoolFeedbackForm()
    return render(request, 'school_supervisor/feedback_form.html', {'form': form, 'student': student})

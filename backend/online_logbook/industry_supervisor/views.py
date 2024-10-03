from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import IndustrySupervisor
from student.models import Student
from .forms import IndustryFeedbackForm

def industry_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('industry_dashboard')
        else:
            return render(request, 'industry_supervisor/login.html', {'error': 'Invalid login credentials'})
    return render(request, 'industry_supervisor/login.html')

def industry_dashboard(request):
    return render(request, 'industry_supervisor/dashboard.html')

def view_students(request):
    supervisor = request.user.industrysupervisor
    students = Student.objects.filter(industry_supervisor=supervisor)
    return render(request, 'industry_supervisor/view_students.html', {'students': students})

def submit_feedback(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = IndustryFeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.student = student
            feedback.industry_supervisor = request.user.industrysupervisor
            feedback.save()
            return redirect('industry_dashboard')
    else:
        form = IndustryFeedbackForm()
    return render(request, 'industry_supervisor/feedback_form.html', {'form': form, 'student': student})

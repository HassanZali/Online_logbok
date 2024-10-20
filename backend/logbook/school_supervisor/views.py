# school_supervisor/views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm


def login(request):
    return render(request, 'school_supervisor/login.html')

def dashboard(request):
    return render(request, 'school_supervisor/dashboard.html')

def students(request):
    return render(request, 'school_supervisor/students.html')

def feedback(request, student_id):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.student_id = student_id  # associate the feedback with the student
            feedback.supervisor = request.user.schoolsupervisor  # associate with the logged-in supervisor
            feedback.save()
            return redirect('school_supervisor:students')
    else:
        form = FeedbackForm()
    return render(request, 'school_supervisor/feedback.html', {'form': form})

def logout(request):
    return redirect('school_supervisor:login')

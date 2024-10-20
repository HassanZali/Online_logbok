# industry_supervisor/views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def login(request):
    return render(request, 'industry_supervisor/login.html')

def dashboard(request):
    return render(request, 'industry_supervisor/dashboard.html')

def students(request):
    # Assume the supervisor can see all students they supervise
    return render(request, 'industry_supervisor/students.html')

def feedback(request, student_id):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.student_id = student_id  # associate the feedback with the student
            feedback.supervisor = request.user.industrysupervisor  # associate with the logged-in supervisor
            feedback.save()
            return redirect('industry_supervisor:students')
    else:
        form = FeedbackForm()
    return render(request, 'industry_supervisor/feedback.html', {'form': form})


def logout(request):
    return redirect('industry_supervisor:login')
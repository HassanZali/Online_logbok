from django.shortcuts import render, redirect
from .models import LogbookEntry
from .forms import LogbookForm, StudentForm

def login(request):
    return render(request, 'student/login.html')

def dashboard(request):
    return render(request, 'student/dashboard.html')

def logbook(request):
    if request.method == 'POST':
        form = LogbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:dashboard')
    else:
        form = LogbookForm()
    return render(request, 'student/logbook.html', {'form': form})

def form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:dashboard')
    else:
        form = StudentForm()
    return render(request, 'student/form.html', {'form': form})

def news(request):
    return render(request, 'student/news.html')

def logout(request):
    return redirect('student:login')

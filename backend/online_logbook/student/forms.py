from django import forms
from .models import DailyLog, Student

class DailyLogForm(forms.ModelForm):
    class Meta:
        model = DailyLog
        fields = ['date', 'activity_description']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course', 'institution', 'year_of_study']

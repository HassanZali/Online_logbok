from django import forms
from .models import Student, LogbookEntry

class LogbookForm(forms.ModelForm):
    class Meta:
        model = LogbookEntry
        fields = ['date', 'entry']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course', 'institution', 'year_of_study', 'phone', 'bank_name', 'account_number']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

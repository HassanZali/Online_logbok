from django import forms
from .models import SchoolFeedbackForm

class SchoolFeedbackForm(forms.ModelForm):
    class Meta:
        model = SchoolFeedbackForm
        fields = ['company_participation', 'student_involvement', 'performance_assessment']

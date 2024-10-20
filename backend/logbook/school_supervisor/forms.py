# school_supervisor/forms.py
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback', 'grade']
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 5}),
            'grade': forms.TextInput(attrs={'placeholder': 'Grade (e.g., A, B, C)'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

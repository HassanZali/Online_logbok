from django import forms
from .models import IndustryFeedbackForm

class IndustryFeedbackForm(forms.ModelForm):
    class Meta:
        model = IndustryFeedbackForm
        fields = ['punctuality', 'dedication', 'initiative', 'general_conduct', 'overall_satisfaction']

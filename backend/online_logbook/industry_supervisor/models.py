from django.db import models
from student.models import Student, User

class IndustrySupervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)

class IndustryFeedbackForm(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    industry_supervisor = models.ForeignKey(IndustrySupervisor, on_delete=models.CASCADE)
    punctuality = models.IntegerField()
    dedication = models.IntegerField()
    initiative = models.IntegerField()
    general_conduct = models.IntegerField()
    overall_satisfaction = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

# industry_supervisor/models.py
from django.db import models
from student.models import Student

class IndustrySupervisor(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)

class Feedback(models.Model):
    supervisor = models.ForeignKey(IndustrySupervisor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='industry_feedbacks')
    feedback = models.TextField()
    grade = models.CharField(max_length=2)

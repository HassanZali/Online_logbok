# school_supervisor/models.py
from django.db import models
from student.models import Student

class SchoolSupervisor(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)

class Feedback(models.Model):
    supervisor = models.ForeignKey(SchoolSupervisor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='school_feedbacks')
    feedback = models.TextField()
    grade = models.CharField(max_length=2)

from django.db import models
from student.models import Student, User
class SchoolSupervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

class SchoolFeedbackForm(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school_supervisor = models.ForeignKey(SchoolSupervisor, on_delete=models.CASCADE)
    company_participation = models.TextField()
    student_involvement = models.TextField()
    performance_assessment = models.CharField(max_length=2)  # e.g., A, B, C, D
    created_at = models.DateTimeField(auto_now_add=True)

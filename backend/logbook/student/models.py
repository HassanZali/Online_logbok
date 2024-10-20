from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    phone = models.CharField(max_length=15)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    industry_supervisor = models.ForeignKey('industry_supervisor.IndustrySupervisor', on_delete=models.SET_NULL, null=True)
    school_supervisor = models.ForeignKey('school_supervisor.SchoolSupervisor', on_delete=models.SET_NULL, null=True)

class LogbookEntry(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    entry = models.TextField()

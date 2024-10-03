from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year_of_study = models.IntegerField()

    def __str__(self):
        return self.name

class DailyLog(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    activity_description = models.TextField()

    def __str__(self):
        return f"{self.student.name} - {self.date}"

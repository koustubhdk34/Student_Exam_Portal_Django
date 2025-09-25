from django.db import models
from django.contrib.auth.models import User

# Extend User model if needed
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    whatsapp = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.user.username

class Exam(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    duration_minutes = models.IntegerField()
    fee = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    result_marks = models.IntegerField(blank=True, null=True)
    admit_card = models.FileField(upload_to='admit_cards/', blank=True, null=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.exam.title}"

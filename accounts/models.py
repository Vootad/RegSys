from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('professor', 'Professor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.student_number


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    professor_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.professor_code

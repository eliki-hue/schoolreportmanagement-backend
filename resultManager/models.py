from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='scores')
    subject = models.CharField(max_length=255)
    score = models.IntegerField()
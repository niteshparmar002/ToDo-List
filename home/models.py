from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDescription = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.taskTitle

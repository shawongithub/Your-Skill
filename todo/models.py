from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TodoList(models.Model):
    user=models.ForeignKey(User,related_name='author',on_delete=models.CASCADE)
    task=models.CharField(max_length=250)

    def __str__(self):
        return self.task
    
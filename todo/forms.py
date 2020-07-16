from django import forms 
from . models import TodoList


class TaskCreation(forms.ModelForm):
    class Meta:
        model=TodoList
        fields=['task']
"""
Defines the TaskForm class for creating and handling task-related forms.

The TaskForm is a ModelForm based on the Task model.
It includes a single field 'task_text' for the user to input task descriptions.
"""
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  # Specifies the model to be used for the form.
        fields = ['task_text']  # Determines which fields from the model should be included in the form.


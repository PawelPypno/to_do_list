"""
Defines the Task model for storing tasks in the database.

A task has a description (task_text) and a status indicating whether it's completed (completed).
"""
from django.db import models

class Task(models.Model):
    task_text = models.CharField(max_length=200)  # Defines a field to store the task description.
    completed = models.BooleanField(default=False)  # Indicates whether the task has been completed or not.

    def __str__(self):
        return self.task_text  # Returns the task description when the object is converted to a string.


"""
Defines view functions for managing tasks.

- `task_list(request)`: Displays the list of tasks and handles task creation.
- `delete_task(request, task_id)`: Deletes a specific task based on its ID.
"""

from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

def task_list(request):
    """
    Displays the list of tasks and handles task creation.
    """
    tasks = Task.objects.all()  # Retrieves all tasks from the database.
    form = TaskForm()  # Instantiates an empty form for creating new tasks.

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the new task to the database.
            return redirect('task_list')  # Redirects back to the task list page after task creation.

    return render(request, 'todo_app/task_list.html', {'tasks': tasks, 'form': form})

def delete_task(request, task_id):
    """
    Deletes a specific task based on its ID.
    """
    task = Task.objects.get(pk=task_id)  # Retrieves the task from the database using its ID.
    task.delete()  # Deletes the task.
    return redirect('task_list')  # Redirects back to the task list page after task deletion.


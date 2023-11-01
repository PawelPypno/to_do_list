/*
Handles the functionality of the delete button and checkbox.

- Delete button functionality:
    - Extracts task ID from the data attribute.
    - Retrieves the list item containing the task.
    - Obtains the CSRF token from the hidden input field.
    - Sends a DELETE request to delete the task.
    - Removes the task from the view if the server responds successfully.

- Checkbox functionality:
    - Toggles the 'completed-task' class based on checkbox status (checked or unchecked).
*/

// Delete button functionality
document.querySelectorAll('.delete-button').forEach(button => {
    button.addEventListener('click', function() {
        // Get task ID from data attribute
        const taskId = this.getAttribute('data-taskid');
        // Get the list item containing the task
        const listItem = this.closest('li');
        // Get CSRF token from the hidden input field
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        // Send DELETE request to delete the task
        fetch(`/delete-task/${taskId}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrftoken,
            },
        })
        .then(response => {
            if (response.ok) {
                // If the server responds successfully, remove the task from the view
                listItem.remove();
            }
        })
        .catch(error => console.error('Error:', error));
    });
});

// Checkbox functionality
document.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        // Get the span element next to the checkbox (contains the task text)
        const taskText = this.nextElementSibling;
        // Toggle the 'completed-task' class based on checkbox status (checked or unchecked)
        taskText.classList.toggle('completed-task', this.checked);
    });
});

#!/usr/bin/python3
"""
    Using a REST API, and a given emp_ID, return info about their TODO list.
"""

import requests
import sys

if __name__ == "__main__":
    """
        The user ID is passed as a command-line argument
    """
	user_id = sys.argv[1]

	"""
        URLs to fetch user and todo data from JSONPlaceholder API
    """
	user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
	todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

	"""
        Fetch user data from the API and parse it as JSON
    """
	users = requests.get(user_url).json()

	"""
        Fetch todos data from the API and parse it as JSON
    """
	todos = requests.get(todo_url).json()

	"""
        Initialize variables to count completed todos and store their titles
    """
	completed_todos = 0
	done_todos = []

	"""
    Get the employee's name from the user data
    """
	employee_name = users.get("name")

	"""
        Iterate through the list of todos
    """
	for todo in todos:
    		if todo.get("completed"):
        	"""
                If the todo is completed, increment the counter and add its title to the list
            """
        	completed_todos += 1
        	done_todos.append(todo.get("title"))

	"""
        Print the employee's name and the number of completed tasks
    """
	print(f"Employee {employee_name} is done with tasks({completed_todos}/20):")

	"""
        Print the titles of completed tasks
    """
	for x in done_todos:
    		print("\t ", x)

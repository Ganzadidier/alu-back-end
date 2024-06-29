#!/usr/bin/python3
import requests
import sys

user_id = sys.argv[1]

user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

users = requests.get(user_url).json()

todos = requests.get(todo_url).json()

completed_todos = 0
done_todos = []

employee_name = users.get("name")


for todo in todos:
    if todo.get("completed"):
        # print("\t ", todo["title"])
        completed_todos += 1
        done_todos.append(todo.get("title"))

print(f"Employee {employee_name} is done with tasks({completed_todos}/20):")
for x in done_todos:
    print("\t ", x)

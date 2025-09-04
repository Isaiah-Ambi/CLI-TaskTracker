import sys
import json
from datetime import datetime

command = sys.argv[1]

def add_task(task):
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            print("Data read successfully:", tasks)
    except FileNotFoundError:
        print("tasks.json not found. Creating an empty dataset.")
        tasks = []
    except json.JSONDecodeError:
        print("Error decoding JSON from tasks.json. Starting with an empty dataset.")
        tasks = []

    new_id = 0
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]['id'] + 1
    new_task = {
        'id': new_id,
        'description': task,
        'created_at': datetime.now().isoformat(),
        'updated_at': None,
        'status': 'todo'
    }
    tasks.append(new_task)
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Added task with ID: {new_id}")

def update_task(task_id, new_task):
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("tasks.json not found. Cannot update task.")
        return
    except json.JSONDecodeError:
        print("Error decoding JSON from tasks.json. Cannot update task.")
        return
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_task
            task['updated_at'] = datetime.now().isoformat()
            break
    else:
        print(f"No task found with ID: {task_id}")
        return
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Updated task ID: {task_id}")

def delete_task(task_id):
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("tasks.json not found. Cannot delete task.")
        return
    except json.JSONDecodeError:
        print("Error decoding JSON from tasks.json. Cannot delete task.")
        return
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            del tasks[i]
            break
    else:
        print(f"No task found with ID: {task_id}")
        return
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Deleted task ID: {task_id}")


def list_tasks():
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
        for task in tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}, Status: {task['status']}")
            # print(task['id'])

def mark_in_progress(task_id):
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("tasks.json not found. Cannot mark task as done.")
        return
    except json.JSONDecodeError:
        print("Error decoding JSON from tasks.json. Cannot mark task as done.")
        return
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'in-progress'
            task['updated_at'] = datetime.now().isoformat()
            break
    else:
        print(f"No task found with ID: {task_id}")
        return
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Marked task ID: {task_id} as done")
    
def mark_done(task_id):
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("tasks.json not found. Cannot mark task as done.")
        return
    except json.JSONDecodeError:
        print("Error decoding JSON from tasks.json. Cannot mark task as done.")
        return
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            task['updated_at'] = datetime.now().isoformat()
            break
    else:
        print(f"No task found with ID: {task_id}")
        return
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Marked task ID: {task_id} as done")

def get_completed_tasks():
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
        completed_tasks = [task for task in tasks if task['done']]
        for task in completed_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}")

def get_in_progress_tasks():
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
        in_progress_tasks = [task for task in tasks if not task['done']]
        for task in in_progress_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}")

def todo_tasks():
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
        todo_tasks = [task for task in tasks if task['status'] == 'todo']
        for task in todo_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}")

# print(sys.argv[1])

def main():
    try:
        if command == 'add':
            task = sys.argv[2]
            add_task(task)
        elif command == 'update':
            task_id = int(sys.argv[2])
            new_task = sys.argv[3]
            update_task(task_id, new_task)
        elif command == 'delete':
            task_id = int(sys.argv[2])
            delete_task(task_id)
        elif command == 'list':
            list_tasks()
        elif command == 'mark-in-progress':
            task_id = int(sys.argv[2])
            mark_in_progress(task_id)
        elif command == 'mark-done':
            task_id = int(sys.argv[2])
            mark_done(task_id)
        elif command == 'list todo':
            todo_tasks()
        elif command == 'list done':
            get_completed_tasks()
        elif command == 'list in-progress':
            get_in_progress_tasks()
        else:
            print("Unknown command")
    except IndexError:
        print("Insufficient arguments provided")


if __name__ == "__main__":
    main()
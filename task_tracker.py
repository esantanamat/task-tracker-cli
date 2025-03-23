import json
import os
import argparse

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
        
        return []
    
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks,file, indent=1)
def add_task(task):
    tasks = load_tasks()

    new_id = max([task["id"] for task in tasks], default=0) + 1
    new_task = {
        "id": new_id,
        "description": task,
        "status": "created"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'added new task')
def remove_task(task_id):
    tasks = load_tasks()
    f_tasks = [task for task in tasks if task["id"] != task_id]

    if len(tasks) == len(f_tasks):
        print(f'Task {task_id} not found')
        return
    
    save_tasks(f_tasks)
    print('Task removed successfully')
def list_tasks():
    tasks = load_tasks()
    descriptions = [task["description"] for task in tasks]
    print(descriptions)    
def list_uncompleted_tasks():
    tasks = load_tasks()
    f_tasks = [task["description"] for task in tasks if task["status"] != "completed"]
    print(f_tasks)    

def list_completed_tasks():
    tasks = load_tasks()
    f_tasks = [task["description"] for task in tasks if task["status"] == "completed"]
    print(f_tasks)    

def list_in_progress_tasks():
    tasks = load_tasks()
    f_tasks = [task["description"] for task in tasks if task["status"] == "in progress"]
    print(f_tasks)    


def update_status(task_id, update):
    tasks = load_tasks()
    t_task = [task for task in tasks if task["id"] == task_id]
    if t_task:
        t_task[0]['status'] = update
        save_tasks(tasks)
        print('Task updated successfully')
    else:
        print('Task not found')



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

   
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task to add")

    
    remove_parser = subparsers.add_parser("remove", help="Remove a task by ID")
    remove_parser.add_argument("task_id", type=int, help="ID of the task to remove")

    # List tasks
    subparsers.add_parser("list", help="List all tasks")
    subparsers.add_parser("list uncomplete", help="List all tasks")
    subparsers.add_parser("list completed", help="List all tasks")
    subparsers.add_parser("list in progress", help="List all tasks")
    update_parser = subparsers.add_parser("update", help = "Update a task")
    update_parser.add_argument("task_id", type=int)
    update_parser.add_argument("update", type=str)

    # Parse arguments
    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "remove":
        remove_task(args.task_id)
    elif args.command == "list":
        list_tasks()
    elif args.command == "update":
        update_status(args.task_id, args.update)
    elif args.command == "list uncomplete":
        list_uncompleted_tasks()
    elif args.command == "list completed":
        list_completed_tasks()
    elif args.command == "list in progress":
        list_in_progress_tasks()

    
# Task Tracker CLI

A simple Command-Line Interface (CLI) tool for managing tasks using Python. This project allows you to add, remove, update, and list tasks. The tasks are stored in a `tasks.json` file in JSON format.

## Features

- **Add a new task** with a description.
- **Remove a task** by its ID.
- **List all tasks**.
- **List incomplete tasks**, tasks that are "in progress", and tasks that are "completed".
- **Update the status** of a task (statuses include: `created`, `in progress`, `completed`).

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/task-tracker-cli.git
2. Navigate to the project directory:

   cd task-tracker-cli
3. Ensure python is installed
## Usage
To add a task: python task_tracker.py add "Your task here"  
To remove a task: python task_tracker.py remove "your task id here as int"  
To list all tasks: python task_tracker.py list  
To list all incomplete tasks (tasks that are not marked as "completed"): python task_tracker.py list_incomplete  
To list all completed tasks: python task_tracker.py list_completed  
To list tasks that are currently in progress: python task_tracker.py list_in_progress  
To update the status of a task, for example, changing it to "in progress": python task_tracker.py update 1 in progress  
Note: Replace 1 with the task's ID and choose from one of the following statuses: created, in progress, completed.  

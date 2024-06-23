import argparse


def add_task(task, file_name='tasks.txt'):
    # Open the file in append mode ('a') to add a new task at the end of the file
    with open(file_name, 'a') as file:
        file.write(task + '\n')  # Write the task followed by a newline character


def view_tasks(file_name='tasks.txt'):
    try:
        # Open the file in read mode ('r') to read the tasks
        with open(file_name, 'r') as file:
            tasks = file.readlines()  # Read all lines (tasks) into a list
            if not tasks:
                print("No tasks found.")  # Inform the user if there are no tasks
            for i, task in enumerate(tasks, start=1):  # Enumerate the tasks, starting index at 1
                print(f"{i}. {task.strip()}")  # Print each task with its number
    except FileNotFoundError:
        print("No tasks found.")  # Inform the user if the file doesn't exist


def delete_task(task_number, file_name='tasks.txt'):
    try:
        # Open the file in read mode to read the tasks
        with open(file_name, 'r') as file:
            tasks = file.readlines()  # Read all lines (tasks) into a list
        if 0 < task_number <= len(tasks):
            del tasks[task_number - 1]  # Delete the task with the specified number
            # Open the file in write mode to overwrite it with the remaining tasks
            with open(file_name, 'w') as file:
                file.writelines(tasks)  # Write the remaining tasks back to the file
            print(f"Deleted task {task_number}.")  # Inform the user that the task was deleted
        else:
            print("Invalid task number.")  # Inform the user if the task number is invalid
    except FileNotFoundError:
        print("No tasks found.")  # Inform the user if the file doesn't exist


def main():
    # Create the top-level parser
    parser = argparse.ArgumentParser(description='Command-line To-Do List Application')
    
    # Add subparsers for the sub-commands
    subparsers = parser.add_subparsers(dest='command')
    
    # Create the parser for the 'add' command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('task', type=str, help='The task description')
    
    # Create the parser for the 'view' command
    view_parser = subparsers.add_parser('view', help='View all tasks')
    
    # Create the parser for the 'delete' command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('task_number', type=int, help='The task number to delete')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Determine which command was issued and call the appropriate function
    if args.command == 'add':
        add_task(args.task)  # Call add_task() with the provided task description
    elif args.command == 'view':
        view_tasks()  # Call view_tasks() to display all tasks
    elif args.command == 'delete':
        delete_task(args.task_number)  # Call delete_task() with the provided task number
    else:
        parser.print_help()  # Print the help message if no valid command was provided

# Ensure the script runs only if it is executed directly (not imported as a module)
if __name__ == '__main__':
    main()

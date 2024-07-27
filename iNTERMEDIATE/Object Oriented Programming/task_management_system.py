from datetime import datetime


class Task:
    def __init__(self, title, description, deadline=None):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def complete_task(self):
        self.completed = True
        print(f"Task '{self.title}' marked as completed.")

    def set_deadline(self, deadline):
        self.deadline = deadline
        print(f"Deadline for task '{self.title}' set to {self.deadline}.")

    def __str__(self):
        return f"Task('{self.title}', '{self.description}', {self.deadline}, {'Completed' if self.completed else 'Pending'})"


class WorkTask(Task):
    def __init__(self, title, description, deadline=None, priority='Normal'):
        super().__init__(title, description, deadline)
        self.priority = priority

    def set_priority(self, priority):
        self.priority = priority
        print(f"Priority for work task '{self.title}' set to {self.priority}.")

    def __str__(self):
        return f"WorkTask('{self.title}', '{self.description}', {self.deadline}, {self.priority}, {'Completed' if self.completed else 'Pending'})"


class PersonalTask(Task):
    def __init__(self, title, description, deadline=None, location=''):
        super().__init__(title, description, deadline)
        self.location = location

    def set_location(self, location):
        self.location = location
        print(f"Location for personal task '{self.title}' set to {self.location}.")

    def __str__(self):
        return f"PersonalTask('{self.title}', '{self.description}', {self.deadline}, {self.location}, {'Completed' if self.completed else 'Pending'})"


def main():
    # Create a work task
    work_task = WorkTask("Complete report", "Finish the quarterly report", deadline="2024-06-30", priority="High")

    # Create a personal task
    personal_task = PersonalTask("Buy groceries", "Buy milk, eggs, and bread", deadline="2024-06-25",
                                 location="Supermarket")

    # Perform operations on work task
    work_task.complete_task()
    work_task.set_deadline("2024-06-29")
    work_task.set_priority("Medium")

    # Perform operations on personal task
    personal_task.set_location("Local market")
    personal_task.complete_task()

    # Print task details
    print(work_task)
    print(personal_task)


if __name__ == "__main__":
    main()



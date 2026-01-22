# Task Management System
# Created by Soumya

tasks = [ ]

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def update_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to update: "))
        new_task = input("Enter new task description: ")
        tasks[task_num - 1] = new_task
        save_tasks()
        print("Task updated successfully!")
    except (ValueError, IndexError):
        print("Invalid input!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        tasks.pop(task_num - 1)
        save_tasks()
        print("Task deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid input!")

def menu():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

load_tasks()#
menu()

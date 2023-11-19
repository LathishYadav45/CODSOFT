import os

def display_menu():
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_todo_list():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            print("To-Do List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
        else:
            print("Your to-do list is empty.")

def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def mark_completed():
    view_todo_list()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            completed_task = tasks.pop(task_number - 1)
            with open("completed.txt", "a") as completed_file:
                completed_file.write(completed_task)
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_todo_list()
    try:
        task_number = int(input("Enter the task number to delete: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted:", deleted_task.strip())
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if not os.path.isfile("todo.txt"):
    with open("todo.txt", "w"):
        pass
if not os.path.isfile("completed.txt"):
    with open("completed.txt", "w"):
        pass

    main()

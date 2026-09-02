from task_manager_app import Task, read_tasks, write_tasks
from task_manager_app.input_validator import (
    validate_string_input,
    validate_priority,
    validate_task_index,
    validate_confirmation
)


def display_menu():
    print("\n" + "=" * 40)
    print("       TASK MANAGER APPLICATION")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 40)


def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return False

    print("\n" + "=" * 60)
    print("                 YOUR CURRENT TASKS")
    print("=" * 60)

    for index, task in enumerate(tasks, start=1):
        print(f"\nTask #{index}")
        print(f"Name        : {task.name}")
        print(f"Description : {task.description}")
        print(f"Priority    : {task.priority}")
        print("-" * 60)

    return True


def add_task(tasks):
    print("\n--- Add New Task ---")

    name = validate_string_input(
        "Enter task name: ",
        r"[A-Za-z0-9][A-Za-z0-9 _-]*"
    )

    description = validate_string_input(
        "Enter task description: "
    )

    priority = validate_priority()

    task = Task(name, description, priority)
    tasks.append(task)

    if write_tasks(tasks):
        print(f"Task '{name}' added successfully!")
    else:
        tasks.pop()
        print("Task creation failed.")


def update_task(tasks):
    print("\n--- Update Task ---")

    if not display_tasks(tasks):
        return

    index = validate_task_index(
        "Enter task number to update: ",
        len(tasks)
    )

    task = tasks[index]

    print("\nPress Enter to keep the existing value.")

    new_name = validate_string_input(
        f"New name [{task.name}]: ",
        r"[A-Za-z0-9][A-Za-z0-9 _-]*",
        allow_blank=True
    )

    new_description = validate_string_input(
        f"New description [{task.description}]: ",
        allow_blank=True
    )

    while True:
        new_priority = input(
            f"New priority [{task.priority}] (High/Medium/Low): "
        ).strip()

        if new_priority == "":
            new_priority = task.priority
            break

        new_priority = new_priority.capitalize()

        if new_priority in ["High", "Medium", "Low"]:
            break

        print("Invalid priority. Please enter High, Medium, or Low.")

    old_values = task.name, task.description, task.priority

    if new_name:
        task.name = new_name

    if new_description:
        task.description = new_description

    task.priority = new_priority

    if write_tasks(tasks):
        print(f"Task '{task.name}' updated successfully!")
    else:
        task.name, task.description, task.priority = old_values
        print("Task update failed.")


def delete_task(tasks):
    print("\n--- Delete Task ---")

    if not display_tasks(tasks):
        return

    index = validate_task_index(
        "Enter task number to delete: ",
        len(tasks)
    )

    task = tasks[index]

    confirmation = validate_confirmation(
        f"Are you sure you want to delete '{task.name}'? (y/n): "
    )

    if confirmation == "n":
        print("Deletion cancelled.")
        return

    deleted_task = tasks.pop(index)

    if write_tasks(tasks):
        print(f"Task '{deleted_task.name}' deleted successfully!")
    else:
        tasks.insert(index, deleted_task)
        print("Task deletion failed.")


def main():
    tasks = read_tasks()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            update_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()